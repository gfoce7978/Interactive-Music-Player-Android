from flask import Flask
import flask
import os 
from werkzeug.utils import secure_filename
import subprocess
from flask import jsonify
from flask import request
UPLOAD_FOLDER = '/home/junaid/Desktop/Emotion-detection-master/Emotion-detection-master/Tensorflow'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
  return 'Server Works!'
  
@app.route('/greet')
def say_hello():
	# getVersion =  subprocess.Popen("python emotions.py --mode value.jpg", shell=True, stdout=subprocess.PIPE).stdout
 #   	version =  getVersion.read()
	# print("My version is", version.decode())
	#myresult = os.system('python emotions.py --mode Test.jpg')
	#print("myresult")
	#print(myresult)
	return 'Hello from Server'
@app.route('/greet', methods=['POST'])
def say_hello2():
 	print("I am called")
 	#print(flask.request.files.get('imageFile', ''))
 	file = flask.request.files.get('imageFile', '')
 	print(file)
 	if(not file):
 		return("Image Is null")
 	if file :
		    filename = secure_filename(file.filename)
		    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		    getVersion =  subprocess.Popen("python emotions.py --mode "+filename, shell=True, stdout=subprocess.PIPE).stdout
		    version =  getVersion.read()
		    print("My version2 is", version.decode())
		    return (version.decode())
		#return version.decode()
@app.route('/gesture', methods=['POST'])
def say_hello3():
 	print("I am called3")
 	print(flask.request.headers)
 	print(flask.request)
 	
 	print(flask.request.files)
 	file = flask.request.files.get('imageFile', '')
	print("file=") 	
	print(file)
 	if(not file):
 		return("Image Is null")
 	if file :
		    filename = secure_filename(file.filename)
		    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		    getVersion =  subprocess.Popen("python gesture.py --mode "+filename, shell=True, stdout=subprocess.PIPE).stdout
		    version =  getVersion.read()
		    print("My version4 is", version.decode())
		    return (version.decode())
		#return version.decode()		
  

  	return 'Hello from Server2'
