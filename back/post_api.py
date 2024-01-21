import json

from flask import Flask, request, jsonify
import connect
from back.register import register_user

app = Flask(__name__)


@app.route('/addcourse', methods=['POST'])
def addcourse():
    data = request.get_json() #json body
    if 'username' not in data:
        return jsonify({'error': 'Missing username field'}), 400
    elif 'section' not in data:
        return jsonify({'error': 'Missing section field'}), 400
    elif 'courseNum' not in data:
        return jsonify({'error': 'Missing courseNum field'}), 400
    elif 'courseDept' not in data:
        return jsonify({'error': 'Missing courseDept field'}), 400

    term = "2023W2"

    try:
        connect.query(f"INSERT INTO Enrolled VALUES ('{data['username']}', '{term}', '{data['section']}', '{data['courseNum']}', '{data['courseDept']}')")
        return jsonify({'success': 'Course section added'}), 200
    except:
        return jsonify({'error': 'Invalid course addition'}), 400


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json() #json body
    first_name = ""
    last_name = ""
    if 'username' not in data:
        return jsonify({'error': 'Missing username field'}), 400
    elif 'password' not in data:
        return jsonify({'error': 'Missing password field'}), 400
    elif 'firstName' in data:
        first_name = data['firstName']
    elif 'lastName' in data:
        last_name = data['lastName']

    try:
        register_user(data['username'], data['password'], f'{first_name}', f'{last_name}')
        return jsonify({'success': 'User registered'}), 200
    except:
        return jsonify({'error': 'Could not register user'}), 400

@app.route('/addfriend', methods=['POST'])
def addfriend():
    data = request.get_json() #json body
    if 'username' not in data:
        return jsonify({'error': 'Missing username field'}), 400
    elif 'friendUsername' not in data:
        return jsonify({'error': 'Missing friendUsername field'}), 400

    try:
        connect.query(f"INSERT INTO Friends VALUES ('{data['username']}', '{data['friendUsername']}')")
        connect.query(f"INSERT INTO Friends VALUES ('{data['friendUsername']}', '{data['username']}')")
        return jsonify({'success': 'Friend made'}), 200
    except:
        return jsonify({'error': 'Could not make friend'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5001)
