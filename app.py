from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Password for login
PASSWORD = "HOME123321"

# Folder for uploaded images
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Make sure uploads folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Home (index)
@app.route("/")
def index():
    return render_template("index.html")

# Cybersecurity page
@app.route("/cybersecurity")
def cybersecurity():
    return render_template("cybersecurity.html")

# Login page
@app.route("/home/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        password = request.form.get("password")
        if password == PASSWORD:
            return redirect(url_for("rota"))
        else:
            error = "Wrong password! Try again."
    return render_template("login.html", error=error)

# Rota + upload photo
@app.route("/home/rota", methods=["GET", "POST"])
def rota():
    if request.method == "POST":
        name = request.form.get("name")
        file = request.files.get("photo")
        if file and name:
            filename = secure_filename(f"{name}_{file.filename}")
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
    return render_template("rota.html")

# Run the app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
