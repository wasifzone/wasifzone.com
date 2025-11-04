from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Simple login password
PASSWORD = "HOME123321"

# Folder to store uploads
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Housemates and their assigned days
housemates = {
    "Ijaz Rauf": "Monday",
    "Shehryar": "Tuesday",
    "Wasif": "Wednesday",
    "Samad": "Thursday",
    "Zahid": "Friday",
    "Imran": "Saturday",
    "Combine": "Sunday"
}

# Home login page
@app.route('/home/login', methods=['GET', 'POST'])
def home_login():
    error = None
    if request.method == 'POST':
        password = request.form.get('password')
        if password == PASSWORD:
            return redirect(url_for('home_rota'))
        else:
            error = "Wrong password! Try again."
    return render_template('login.html', error=error)

# Home rota page
@app.route('/home/rota', methods=['GET', 'POST'])
def home_rota():
    if request.method == 'POST':
        # Get which housemate's upload was submitted
        housemate = request.form.get('housemate')
        file = request.files.get('file')
        if housemate and file:
            # Create folder for housemate if doesn't exist
            housemate_folder = os.path.join(UPLOAD_FOLDER, housemate)
            os.makedirs(housemate_folder, exist_ok=True)
            # Save file
            file.save(os.path.join(housemate_folder, file.filename))
            return redirect(url_for('home_rota'))
    return render_template('rota.html', housemates=housemates)

# Existing routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cybersecurity')
def cybersecurity():
    return render_template('cybersecurity.html')

@app.route('/entertainment')
def entertainment():
    return render_template('entertainment.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
