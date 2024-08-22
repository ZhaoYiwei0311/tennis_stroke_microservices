from sqlalchemy import and_

from relational_data_service.models.video import Video
from relational_data_service.db import db
from flask import Blueprint, jsonify, request, make_response

import relational_data_service.services.videos_service as video_service

video_bp = Blueprint('video_bp', __name__)

@video_bp.get('/get_videos_by_user_id')
def get_videos_by_user_id():  # put application's code here
    # Extract query parameters
    user_id = request.args.get('user_id', type=int)

    response = video_service.search_video_by_user_id(user_id)

    return jsonify(response.to_dict())