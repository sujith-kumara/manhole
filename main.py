from flask import *
import os
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('base.html')

@app.route("/login")
def login():
    return render_template('login.html')

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app.config['UPLOAD_FOLDER'] = f"{APP_ROOT}{os.sep}uploads"
@app.route("/upload", methods=["POST", "GET"])
def upload():
    if request.method == "POST":
        f = request.files["file"]
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
    return render_template('upload.html')

@app.route("/complaint")
def complaint():
    return render_template('complaint.html')

@app.route("/admin")
def admin():
    return render_template('admin.html')