from flask import Flask
from decouple import config

app = Flask(__name__)

@app.route("/")
def index():
    return "ALSKLAKSALSKAKSLASKLAKSKLAS"


app.run(host="0.0.0.0", port=config("PORT"))


