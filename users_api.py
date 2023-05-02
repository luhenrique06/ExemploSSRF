from flask import Flask, jsonify, request
from db import db_users


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Hello, USERS API'})


@app.route('/search/', methods=['GET'])
@app.route('/search/<string:query>', methods=['GET'])
def search(query = ''):
    result = list(
        filter(lambda u: query.casefold() in u['name'].casefold(), db_users)
    )

    result = list(
        map(lambda u: {
            "id": u["id"],
            "name": u["name"]
        }, result)
    )

    return {
        'result': result
    }


@app.route('/profile/<string:user_id>', methods=['GET'])
def user_by_id(user_id):
    user = next(
        filter(lambda u: user_id == u['id'], db_users),
        None
    )

    result = user or {}
    status = 200 if user is not None else 404

    return { 'result': result }, status


if __name__ == '__main__':
    app.run(debug=True, port=5002)


