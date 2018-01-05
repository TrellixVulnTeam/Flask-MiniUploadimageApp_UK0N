from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify
from werkzeug import secure_filename
from flask_pymongo import PyMongo
import imageOpenCV
import os
from flask_pymongo import PyMongo

app = Flask(__name__)

# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'JPG'])


@app.route('/')
def index():
    return render_template('index.html')


# Route that will process the file upload
@app.route('/upload', methods=['POST'])
def upload():
    # Get the name of the uploaded file
    file = request.files['file']
    # Make the filename safe, remove unsupported chars
    filename = secure_filename(file.filename)
    # Move the file form the temporal folder to the upload folder we setup
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    # Redirect the user to the uploaded_file route, which
    # will basicaly show on the browser the uploaded file
    # print(filename)
    imageOpenCV.GaussianBlurImg(filename)
    return redirect(url_for('result_file', filename=filename))


@app.route('/uploads/<filename>')
def result_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


# connect with mongoDB
app.config['MONGO_DBNAME'] = 'dbpy'
app.config['MONGO_URI'] = 'mongodb://admin:admin@ds161400.mlab.com:61400/dbpy'

mongo = PyMongo(app)


@app.route('/add')
def add():
    user = mongo.db.user
    user = mongo.db.users
    user.insert({'name': 'Proud'})
    return 'Added new User'


if __name__ == '__main__':
    app.run(debug=True)
