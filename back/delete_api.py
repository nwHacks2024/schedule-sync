import json

from flask import Flask, request, jsonify
import connect
from back.register import register_user

app = Flask(__name__)

@app.route('/removecourse', methods=['DELETE'])
def removecourse():
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
        connect.query(f"DELETE FROM Enrolled WHERE username='{data['username']}' AND term='{term}' AND section='{data['section']}' AND courseNum='{data['courseNum']}' AND courseDept='{data['courseDept']}'")
        return jsonify({'success': 'Course section deleted!'}), 200
    except:
        return jsonify({'error': 'Invalid course deletion'}), 400

@app.route('/removefriend', methods=['DELETE'])
def removefriend():
    data = request.get_json() #json body
    if 'username' not in data:
        return jsonify({'error': 'Missing username field'}), 400
    elif 'friendUsername' not in data:
        return jsonify({'error': 'Missing friendUsername field'}), 400

    try:
        connect.query(f"DELETE FROM Friends WHERE username='{data['username']}' AND friendUsername='{data['friendUsername']}'")
        connect.query(f"DELETE FROM Friends WHERE username='{data['friendUsername']}' AND friendUsername='{data['username']}'")
        return jsonify({'success': 'Friend removed'}), 200
    except:
        return jsonify({'error': 'Could not remove friend'}), 400


if __name__ == '__main__':
    app.run(debug=True, port=5001)
