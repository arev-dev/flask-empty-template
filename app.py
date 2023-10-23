from flask import Flask
from decouple import config


app = Flask(__name__)

@app.route("/")
def index():
    return "ALSKLAKSALSKAKSLASKLAKSKLAS"

if __name__ == '__main__':
    app.run()
    
