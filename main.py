from flask import Flask,render_template, request
from fonction1 import *

app = Flask (__name__)
PORT = 5000
DEBUG = False

@app.errorhandler(404)
def not_found(error):
    return "Not Found."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return fonc(userText)

if __name__ == '__main__' :
    app.run(port = PORT , debug = DEBUG)
    
    
