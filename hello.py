from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello():
     return render_template('index.html')