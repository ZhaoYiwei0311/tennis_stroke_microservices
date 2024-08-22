import jsonpickle
from datetime import datetime

from flask import Flask, jsonify, request
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String, and_
from sqlalchemy.orm import Mapped, mapped_column

from relational_data_service import db
from relational_data_service.models.video import Video
from relational_data_service.routes.video import video_bp


# from relational_data_service.routes.video import blp as VideoBlueprint


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/tennis_stroke_process'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.db.init_app(app)

    app.register_blueprint(video_bp)

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
