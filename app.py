from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Simple login credentials
PASSWORD = "HOME123321"

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
@app.route('/rota')
def rota():
    return render_template('rota.html')

# Upload photo (handle uploaded images)
@app.route('/upload', methods=['POST'])
def upload():
    uploaded_file = request.files.get('photo')
    name = request.form.get('name')
    if uploaded_file and name:
        upload_folder = os.path.join('static', 'uploads', name)
        os.makedirs(upload_folder, exist_ok=True)
        file_path = os.path.join(upload_folder, uploaded_file.filename)
        uploaded_file.save(file_path)
        return redirect(url_for('rota'))
    return "Upload failed. Please try again."

# Existing routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cybersecurity')
def cybersecurity():
    return render_template('cybersecurity.html')

# Run the app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
