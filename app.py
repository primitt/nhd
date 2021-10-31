from flask import Flask
from flask.templating import render_template
app = Flask(__name__, template_folder='/html')

@app.route("/")
def home():
    return render_template("home.html")



