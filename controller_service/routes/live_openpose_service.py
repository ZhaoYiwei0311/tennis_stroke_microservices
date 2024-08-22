
from flask import Flask, jsonify, request, Blueprint
import requests


LIVE_OPENPOSE_SERVICE = 'http://localhost:5002/'

live_openpose_service_bp = Blueprint('live_openpose_service_bp', __name__)

@live_openpose_service_bp.route('/live_catch')
def get_videos_by_user_id():
    user_id = request.args.get('user_id', type=int)
    # print(user_id)
    responses = requests.get(f'{LIVE_OPENPOSE_SERVICE}live_catch',
                             params={'user_id': user_id})
    print(responses.json())
    return responses.json(), responses.status_code