from flask import Flask, jsonify, request, render_template
import requests
import os
import debugpy
from hashlib import md5
debugpy.listen(("0.0.0.0", 5678))


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')



@app.route('/search-users', methods=['GET'])
def search_users():
    query = request.args.get('q')

    users_api_url = f'{os.environ["USERS_API_URL"]}/search/{query}'
    users_response = requests.get(users_api_url)

    return jsonify({
        'result': users_response.json()['result']
    })


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file and allowed_file(file.filename):
        img_bytes = file.read()
        hash_md5 = md5(img_bytes).hexdigest()
        return jsonify({"md5": hash_md5})

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}


if __name__ == '__main__':
    app.run(debug=True, port=5001)