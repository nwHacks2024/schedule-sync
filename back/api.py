import json

from flask import Flask, request, jsonify
import connect

app = Flask(__name__)


@app.route('/userprofile', methods=['GET'])
def userinfo():
    titles = connect.query("SHOW COLUMNS FROM Students")
    data = request.get_json()
    if 'username' not in data:
        return jsonify({'error': 'Missing username field'}), 400

    username = data['username']
    results = connect.query(f"SELECT * FROM Students WHERE username = '{username}'")
    keys = []
    for title in titles:
        if title[0] != 'hashedPassword' and title[0] != 'salt':
            keys.append(title[0])

    values = []
    for entry in results[0]:
        values.append(entry)

    data_dict = dict(zip(keys, values))

    # Convert the dictionary to a JSON-formatted string
    json_data = json.dumps(data_dict)
    return json_data

@app.route('/friends', methods=['GET'])
def friends():
    friend_titles = connect.query("SHOW COLUMNS FROM Friends")
    data = request.get_json() #json body
    if 'username' not in data:
        return jsonify({'error': 'Missing username field'}), 400

    username = data['username']

    record_count = connect.query(f"SELECT COUNT(*) FROM Friends WHERE username = '{username}'")[0][0]
    results = connect.query(f"SELECT * FROM Friends WHERE username = '{username}'")
    dictionary = {}
    dictionary['count'] = record_count

    all_friends = []
    for i in range(record_count):
        keys = []
        for title in friend_titles:
            keys.append(title[0])

        values = []
        if results:
            for entry in results[0]:
                values.append(entry)

        data_dict = dict(zip(keys, values))
        all_friends.append(data_dict)

    dictionary['results'] = all_friends

    # Convert the dictionary to a JSON-formatted string
    json_data = json.dumps(dictionary)
    return json_data

if __name__ == '__main__':
    app.run(debug=True, port=5001)