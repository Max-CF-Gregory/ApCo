from flask import Flask, send_file
from flask_cors import CORS
 
app = Flask(__name__)
CORS(app)
 
@app.route("/")
def index():
    return send_file("html_page.html")
 
@app.route("/style.css")
def style():
    return send_file("style.css", mimetype="text/css")
 
@app.route("/data")
def data():
    return send_file("data.json", mimetype="application/json")
 
if __name__ == "__main__":
    app.run(port=8000)
 