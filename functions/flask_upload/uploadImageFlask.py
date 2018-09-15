from flask import Flask,request,redirect,url_for,send_from_directory,flash
import os,datetime
import numpy as np
from PIL import Image
from flask_httpauth import HTTPBasicAuth
import flask_login
app=Flask(__name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
pDir='\\'
date=datetime.datetime.today().strftime('%Y-%m-%d')
parentDir=os.getcwd().split('\\')[0:-2]
pDir=pDir.join(parentDir)
UPLOAD_FOLDER=pDir+'\\'+'data\\images\\'+date
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
auth=HTTPBasicAuth()
##############################################################UPLOAD IMAGE ##############################################################
def checkDir(imagePath):
    if os.path.exists(imagePath):
        print('Uploaded file will be saved at : '+ imagePath)
    else:
        os.makedirs(imagePath)
        print('Uploaded file will be saved at : '+ imagePath)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
@auth.login_required
def upload_file():
    checkDir(UPLOAD_FOLDER)
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('return_Array',
                                    filename=file.filename))
        else:
            return "File Format Not supported"
    return '''
    <!doctype html>
    <title>Upload Image</title>
    <h1>Upload Image</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Submit>
    </form>
    '''
@app.route('/Array/<filename>')
@auth.login_required
def return_Array(filename):
    imagees=Image.open(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return str(np.array(imagees))
################################################################################ AUTHENTICATION ####################################################################

users={
    "admin": "admin123",
    "vineet": "vineet123"
}


@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

if __name__=='__main__':
    app.secret_key='testing'
    app.run()
