import json

from flask import Flask, request, jsonify
import connect

app = Flask(__name__)


@app.route('/api/userinfo', methods=['GET'])
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

if __name__ == '__main__':
    app.run(debug=True)