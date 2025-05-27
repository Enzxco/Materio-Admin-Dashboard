from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='javascript-version/dist', static_url_path='')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

# Optional: handle Vue routes
@app.errorhandler(404)
def not_found(e):
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
