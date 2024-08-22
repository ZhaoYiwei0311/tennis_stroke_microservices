import asyncio
import logging
import os
import sys
import time
import pickle
import uuid
from platform import platform

import cv2
import redis
from aiortc import RTCSessionDescription, RTCPeerConnection
from flask import Blueprint, request, jsonify, Response

# import live_openpose_service.models.response as Response

live_catch_bp = Blueprint('video_bp', __name__)

my_redis = redis.Redis(port=6379)

# print(f"Published message '{message}' to channel '{channel_name}'")

# Set to keep track of RTCPeerConnection instances
# pcs = set()





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
def generate_frames(user_id):
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

            # draw points
            frame = datum.cvOutputData

            ret, buffer = cv2.imencode('.jpg', frame)

            frame = buffer.tobytes()

            # r.publish(f'image_channel_{user_id}', frame)
            # res = []
            # for k in datum.poseKeypoints:
            #     res.append(k)
            my_redis.publish(f'captures_{user_id}', pickle.dumps(datum.poseKeypoints))
            # Concatenate frame and yield for streaming

            # print(datum.poseKeypoints)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            elapsed_time = time.time() - start_time
            logging.debug(f"Frame generation time: {elapsed_time} seconds")
            # time.sleep(0.1)

            # break
            # print(f"Frame generation time: {elapsed_time} seconds")


# Route to stream video frames
@live_catch_bp.route('/live_catch')
def live_catch():
    user_id = request.args.get('user_id', type=int)

    print(user_id)
    return Response(generate_frames(user_id), mimetype='multipart/x-mixed-replace; boundary=frame')
