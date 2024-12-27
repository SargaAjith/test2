from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/login",methods=['POST','GET'])
def login():
    if request.method == 'POST':

        print("This is login page!")
        return "Returned from post "
    return "Returned from get "

@app.route("/name/<password>",defaults={"username":"guest"},methods=['POST','GET'])
@app.route("/name/<username>/<password>")
def name(username,password):
    if request.method == 'POST':
        return "POST METHOD"
    a = "name is /t" +username +"password is /t" +password
    return a
app.debug = True