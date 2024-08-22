from flask import Flask, request, redirect, url_for, render_template, flash, jsonify, request, Blueprint
import requests
import controller_service.models.response as Response
import controller_service.errors.errors as Errors
import controller_service.errors.errors as errors
import os


UPLOAD_VIDEO_SERVICE = 'http://localhost:5003/'
TEMP_FOLDER_MENU = 'temp/'

upload_video_service_bp = Blueprint('upload_video_service_bp', __name__)

@upload_video_service_bp.post('/upload_video')
def upload_video():
    # Check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return Response.failure(Errors.NO_FILE_UPLOADED_ERROR).to_dict()

    file = request.files['file']

    files = {'file': file}
    if file:
        print(files)
        file_path = os.path.join(TEMP_FOLDER_MENU, file.filename)
        file.save(file_path)

        # Open the file in binary mode and use the correct 'files' parameter
        with open(file_path, 'rb') as file:
            files = {'file': (file_path.split('/')[-1], file, 'multipart/form-data')}
            response = requests.post(f'{UPLOAD_VIDEO_SERVICE}upload_video', files=files)
            return 'success'

    return 'sorry'
    # return redirect(url_for('index'))