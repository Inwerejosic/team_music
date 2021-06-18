from flask import Flask
app = Flask(__name__)

#routes

@app.route("/")
def home():
    return "Hello Flashy!"