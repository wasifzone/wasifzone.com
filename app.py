from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cybersecurity')
def cybersecurity():
    return render_template('cybersecurity.html')

@app.route('/entertainment')
def entertainment():
    return render_template('entertainment.html')

if __name__ == "__main__":
    app.run(debug=True)
