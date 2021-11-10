from flask import Flask
from flask.templating import render_template
app = Flask(__name__, template_folder='html/')

@app.route("/home")
def home():
    return render_template("home.html")
@app.route("/")
def start():
    return render_template("hyper.html")
@app.route("/indepth")
def indepth():
    return render_template("indepth.html")
@app.route("/devcredits")
def indepth():
    return render_template("devcredits.html")
@app.errorhandler(404)
def error404():
    return render_template("404.html")

