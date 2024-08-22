from flask import Flask, jsonify, request
from routes.relational_data_service import relational_data_service_bp
from routes.live_openpose_service import live_openpose_service_bp
import requests

def create_app():
    app = Flask(__name__)
    app.register_blueprint(relational_data_service_bp)
    app.register_blueprint(live_openpose_service_bp)

    return app


app = create_app()

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
