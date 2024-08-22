
from flask import Flask, jsonify, request, Blueprint, Response, stream_with_context
import requests
import redis
import time


LIVE_OPENPOSE_SERVICE = 'http://localhost:5002/'

live_openpose_service_bp = Blueprint('live_openpose_service_bp', __name__)

@live_openpose_service_bp.route('/live_catch')
def live_catch():
    user_id = request.args.get('user_id', type=int)

    # print(user_id)
    responses = requests.get(f'{LIVE_OPENPOSE_SERVICE}live_catch',
                             params={'user_id': user_id})
    return responses.json()

def stream_video(url):
    with requests.get(url, stream=True) as r:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                yield chunk

@live_openpose_service_bp.route('/relay_feed')
def relay_feed():

    return Response(stream_with_context(stream_video('http://localhost:5002/live_catch')),
                    mimetype='multipart/x-mixed-replace; boundary=frame')