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



if __name__ == '__main__':
    app.run(debug=True, port=5001)