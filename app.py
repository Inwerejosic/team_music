#  Flask imports

from flask import Flask
from flask import render_template
from datetime import datetime
import re

app = Flask(__name__)

#routes

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )
hello_there(hello_there)    