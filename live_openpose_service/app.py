from flask import Flask
from routes.live_catch import live_catch_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(live_catch_bp)
    return app

app = create_app()


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
