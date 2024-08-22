import asyncio
import logging
import os
import sys
import time
import uuid
from platform import platform

import cv2
from aiortc import RTCSessionDescription, RTCPeerConnection
from flask import Blueprint, request, jsonify, Response

live_catch_bp = Blueprint('video_bp', __name__)

# Set to keep track of RTCPeerConnection instances
pcs = set()

try:
    # Windows Import

    # Change these variables to point to the correct folder (Release/x64 etc.)
    sys.path.append('E:\\Codes\\CodingRelated\\Python\\libs\\openpose\\openpose\\build\\python\\openpose\\Release')
    os.environ['PATH'] = (os.environ[
                              'PATH'] + ';' +
                          'E:\\Codes\\CodingRelated\\Python\\libs\\openpose\\openpose\\build\\x64\\Release;' +
                          'E:\\Codes\\CodingRelated\\Python\\libs\\openpose\\openpose\\build\\bin;')
    import pyopenpose as op
except ImportError as e:
    print(
        'Error: OpenPose library could not be found. Did you enable `BUILD_PYTHON` in CMake and have this Python script in the right folder?')
    raise e


# @live_catch_bp.route('/live_catch')
def generate_frames():
    params = dict()
    params["model_folder"] = 'E:\\Codes\\CodingRelated\\Python\\libs\\openpose\\openpose\\models'
    camera = cv2.VideoCapture(0)
    # Starting OpenPose
    opWrapper = op.WrapperPython()
    opWrapper.configure(params)
    opWrapper.start()

    while True:
        start_time = time.time()
        success, frame = camera.read()

        # frame_width = int(frame.get(cv2.CAP_PROP_FRAME_WIDTH))
        # frame_height = int(frame.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # print(frame_width, frame_height)
        if not success:
            break
        else:
            datum = op.Datum()

            datum.cvInputData = frame
            opWrapper.emplaceAndPop(op.VectorDatum([datum]))

            frame = datum.cvOutputData

            ret, buffer = cv2.imencode('.jpg', frame)

            frame = buffer.tobytes()
            # Concatenate frame and yield for streaming
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            elapsed_time = time.time() - start_time
            logging.debug(f"Frame generation time: {elapsed_time} seconds")
            print(f"Frame generation time: {elapsed_time} seconds")


async def offer_async():
    params = await request.json
    offer = RTCSessionDescription(sdp=params["sdp"], type=params["type"])

    # Create an RTCPeerConnection instance
    pc = RTCPeerConnection()

    # Generate a unique ID for the RTCPeerConnection
    pc_id = "PeerConnection(%s)" % uuid.uuid4()
    pc_id = pc_id[:8]

    # Create a data channel named "chat"
    # pc.createDataChannel("chat")

    # Create and set the local description
    await pc.createOffer(offer)
    await pc.setLocalDescription(offer)

    # Prepare the response data with local SDP and type
    response_data = {"sdp": pc.localDescription.sdp, "type": pc.localDescription.type}

    return jsonify(response_data)


# Wrapper function for running the asynchronous offer function
def offer():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    future = asyncio.run_coroutine_threadsafe(offer_async(), loop)
    return future.result()

# Route to stream video frames
@live_catch_bp.route('/live_catch')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')