from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Password for home login
PASSWORD = "HOME123321"

# Home login page
@app.route('/home/login', methods=['GET', 'POST'])
def home_login():
    if request.method == 'POST':
        password = request.form['password']
        if password == PASSWORD:
            return redirect(url_for('home_rota'))
        else:
            return "Wrong password! Try again."
    return render_template('login.html')

# Home rota page
@app.route('/home/rota', methods=['GET', 'POST'])
def home_rota():
    if request.method == 'POST':
        # Handle photo upload here
        uploaded_file = request.files.get('photo')
        if uploaded_file:
            uploaded_file.save(os.path.join('static/uploads', uploaded_file.filename))
    return render_template('rota.html')

# Existing pages
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cybersecurity')
def cybersecurity():
    return render_template('cybersecurity.html')

# Run the app
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
