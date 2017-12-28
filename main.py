from flask import Flask, request

app = Flask (__name__)
PORT = 5000
DEBUG = False

@app.errorhandler(404)
def not_found(error):
    return "Not Found."

@app.route("/")
def index():
    return "Hello World!"

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return "i got you question"

if __name__ == '__main__' :
    app.run(port = PORT , debug = DEBUG)
    
    
