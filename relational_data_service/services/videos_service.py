from flask import jsonify
from sqlalchemy import and_

from relational_data_service.models.video import Video
import relational_data_service.models.response as Response
import relational_data_service.errors.errors as Errors

def search_video_by_user_id(user_id):
    query = Video.query
    conditions = []

    try:
        conditions.append(Video.is_deleted == 0)
        if user_id is not None:
            conditions.append(Video.user_id == user_id)

        if conditions:
            query = query.filter(and_(*conditions))
        videos = query.all()

        results = [video.to_dict() for video in videos]

        return Response.success(results)
    except:
        return Response.failure(Errors.SQL_QUERY_FAILED_ERROR)
