
from flask import Flask


from relational_data_service import db

from controllers.video import video_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/tennis_stroke_process'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.db.init_app(app)

    app.register_blueprint(video_bp)

    return app


app = create_app()

if __name__ == '__main__':
    app.run(port=5001)
