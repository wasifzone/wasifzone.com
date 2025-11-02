from flask import Flask, render_template
import os

app = Flask(__name__)

# Homepage route
@app.route('/')
def index():
    return render_template('index.html')

# Add more routes if needed, e.g., for other pages
# @app.route('/another-page')
# def another_page():
#     return render_template('another_page.html')

if __name__ == "__main__":
    # Get the port from the environment variable assigned by Render, default to 5000 locally
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

