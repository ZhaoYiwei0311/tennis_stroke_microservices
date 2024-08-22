
from flask import Flask, jsonify, request, Blueprint
import requests

import controller_service.models.response as Response


RELATIONAL_DATA_SERVICE = 'http://localhost:5001/'

relational_data_service_bp = Blueprint('relational_data_service_bp', __name__)


@relational_data_service_bp.get('/get_videos_by_user_id')
def get_videos_by_user_id():
    user_id = request.args.get('user_id', type=int)
    response = (requests.get(f'{RELATIONAL_DATA_SERVICE}get_videos_by_user_id',
                             params={'user_id': user_id}))

    return response.json()