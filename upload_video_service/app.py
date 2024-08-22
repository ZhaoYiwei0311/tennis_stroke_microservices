from flask import Flask, request, redirect, url_for, render_template, flash
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Set the folder to store the uploaded videos
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Set the allowed extensions for upload
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'mkv'}

# Make sure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# Function to check if the file has an allowed extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('upload.html')


@app.route('/upload_video', methods=['GET', 'POST'])
def upload_file():
    print(request.files)
    if request.method == 'POST':
        # Check if the post request has the file part
        print(request.files)

        file = request.files['file']
        print(file.content_length)
        #
        # # If user does not select a file, the browser also submits an empty part without filename
        # if file.filename == '':
    #     flash('No selected file')
        #     return redirect(request.url)
        #

        print(file.filename)
        # if file and allowed_file(file.filename):
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            return f'successfully: {filename}'

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=5003)