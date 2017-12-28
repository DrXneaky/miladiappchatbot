from flask import Flask

app = Flask (__name__)
PORT = 5000
DEBUG = False

@app.errorhandler(404)
def not_found(error):
    return "Not Found."

@app.route('/', methods=['GET'])
def index():
    sentence = input()
    return "my name is ahmed miladi"

if __name__ == '__main__' :
    app.run(port = PORT , debug = DEBUG)
    
    
