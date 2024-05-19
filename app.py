from flask import Flask, send_from_directory
from src.view.view import submit

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('src/view/', 'index.html')

@app.route('/submit', methods=['POST'])
def submit_route():
    return submit()

if __name__ == "__main__":
    app.run(debug=True)
