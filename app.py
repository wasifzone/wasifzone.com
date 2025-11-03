from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Password for login
PASSWORD = "HOME123321"

# List of housemates and their cleaning days
ROTA = {
    "Monday": "Ijaz",
    "Tuesday": "Shehryar",
    "Wednesday": "Wasif",
    "Thursday": "Samad",
    "Friday": "Zahid",
    "Saturday": "Imran",
    "Sunday": "Combine"
}

UPLOAD_FOLDER = "static/uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        password = request.form.get('password')
        if password == PASSWORD:
            return redirect(url_for('rota'))
        else:
            error = "Wrong password! Try again."
    return render_template('login.html', error=error)

# Rota page
@app.route('/rota', methods=['GET', 'POST'])
def rota():
    if request.method == 'POST':
        username = request.form.get('username')
        file = request.files.get('file')
        if username and file:
            user_folder = os.path.join(UPLOAD_FOLDER, username)
            if not os.path.exists(user_folder):
                os.makedirs(user_folder)
            file.save(os.path.join(user_folder, file.filename))
            return redirect(url_for('rota'))

    return render_template('rota.html', rota=ROTA)

# Homepage
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cybersecurity')
def cybersecurity():
    return render_template('cybersecurity.html')

@app.route('/entertainment')
def entertainment():
    return render_template('entertainment.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
