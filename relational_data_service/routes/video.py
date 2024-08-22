from sqlalchemy import and_

from relational_data_service.models.video import Video
from relational_data_service.db import db
from flask import Blueprint, jsonify, request

video_bp = Blueprint('video_bp', __name__)

@video_bp.get('/get_videos_by_user_id')
def get_videos_by_user_id():  # put application's code here
    # Extract query parameters
    user_id = request.args.get('user_id', type=int)

    query = Video.query
    conditions = []

    conditions.append(Video.is_deleted == 0)
    if user_id is not None:
        conditions.append(Video.user_id == user_id)

    if conditions:
        query = query.filter(and_(*conditions))
    videos = query.all()
    print(videos)
    return jsonify([video.to_dict() for video in videos])