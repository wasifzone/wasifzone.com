from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Simple login password
PASSWORD = "HOME123321"

# Home login page
@app.route('/home/login', methods=['GET', 'POST'])
def home_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if password == PASSWORD:
            # Redirect to rota page after successful login
            return redirect(url_for('home_rota'))
        else:
            return "Wrong password! Try again."
    return render_template('login.html')

# Home rota page
@app.route('/home/rota')
def home_rota():
    return render_template('rota.html')

# Existing routes
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

