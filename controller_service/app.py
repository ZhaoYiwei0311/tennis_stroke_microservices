import redis
import websocket
from flask import Flask, Response
from controllers.relational_data_service import relational_data_service_bp
from controllers.live_openpose_service import live_openpose_service_bp
from controllers.upload_video_service import upload_video_service_bp




def create_app():
    app = Flask(__name__)
    app.register_blueprint(relational_data_service_bp)
    app.register_blueprint(live_openpose_service_bp)
    app.register_blueprint(upload_video_service_bp)
    app.secret_key = "super secret key"

    return app


app = create_app()

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000)
    app.run(host='0.0.0.0', port=5000)
