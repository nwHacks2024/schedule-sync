import json

from flask import Flask, request, jsonify
import connect
import register

app = Flask(__name__)


@app.route('/userprofile', methods=['POST'])
def userinfo():
    titles = connect.query("SHOW COLUMNS FROM Students")
    data = request.get_json()
    if 'username' not in data:
        return jsonify({'error': 'Missing username field'}), 400

    username = data['username']
    count = connect.query(f"SELECT COUNT(*) FROM Students WHERE username = '{username}'")[0][0]
    if count == 0:
        return jsonify({'error': 'Username does not exist'}), 400

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
    return jsonify(data_dict)

@app.route('/friends', methods=['POST'])
def friends():
    friend_titles = connect.query("SHOW COLUMNS FROM Friends")
    data = request.get_json() #json body
    if 'username' not in data:
        return jsonify({'error': 'Missing username field'}), 400

    username = data['username']
    count = connect.query(f"SELECT COUNT(*) FROM Students WHERE username = '{username}'")[0][0]
    if count == 0:
        return jsonify({'error': 'Username does not exist'}), 400

    record_count = connect.query(f"SELECT COUNT(*) FROM Friends WHERE username = '{username}'")[0][0]
    results = connect.query(f"SELECT * FROM Friends WHERE username = '{username}'")
    dictionary = {}
    dictionary['count'] = record_count

    keys = []
    for j in range(1, len(friend_titles)):
        title = friend_titles[j]
        keys.append(title[0])

    all_friends = []

    for i in range(0, record_count):
        values = []
        if results:
            values.append(results[i][1])

        data_dict = dict(zip(keys, values))
        all_friends.append(data_dict)

    dictionary['results'] = all_friends

    # Convert the dictionary to a JSON-formatted string
    return jsonify(dictionary)

@app.route('/registeredcourses', methods=['POST'])
def registeredcourses():
    data = request.get_json() #json body

    if 'username' not in data:
        return jsonify({'error': 'Missing username field'}), 400

    username = data['username']

    enrolled_titles = connect.query("SHOW COLUMNS FROM Enrolled")

    count = connect.query(f"SELECT COUNT(*) FROM Students WHERE username = '{username}'")[0][0]
    if count == 0:
        return jsonify({'error': 'Username does not exist'}), 400

    record_count = connect.query(f"SELECT COUNT(*) FROM Enrolled WHERE username = '{username}'")[0][0]
    results = connect.query(f"SELECT * FROM Enrolled WHERE username = '{username}' AND Term = '2023W2'")
    dictionary = {}
    dictionary['count'] = record_count

    keys = []
    print(enrolled_titles)
    for j in range(1, len(enrolled_titles)):
         title = enrolled_titles[j]
         keys.append(title[0])

    all_enrollments = []
    print(results)
    for i in range(0, record_count):
        values = []
        if results:
            current = results[i]
            for j in range(1, len(current)):
                values.append(current[j])

        data_dict = dict(zip(keys, values))
        all_enrollments.append(data_dict)

    dictionary['results'] = all_enrollments

    # Convert the dictionary to a JSON-formatted string
    return jsonify(dictionary)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json() #json body
    if 'username' not in data:
        return jsonify({'error': 'Missing username field'}), 400
    if 'password' not in data:
        return jsonify({'error': 'Missing password field'}), 400

    username = data['username']
    password = data['password']

    count = connect.query(f"SELECT COUNT(*) FROM Students WHERE username = '{username}'")[0][0]
    if count == 0:
        return jsonify({'error': 'Username does not exist'}), 400

    if(register.authenticate_user(username, password)):
        return jsonify({'success': 'Login successful'}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/users', methods=['POST'])
def users():
    data = request.get_json()
    if 'username' not in data:
        return jsonify({'error': 'Missing username field'}), 400
    if 'searchName' not in data:
        return jsonify({'error': 'Missing searchName field'}), 400

    titles = connect.query("SHOW COLUMNS FROM Students")

    username = data['username']
    searchName = data['searchName']
    count = connect.query(f"SELECT COUNT(*) FROM Students WHERE username = '{username}'")[0][0]
    if count == 0:
        return jsonify({'error': 'Username does not exist'}), 400

    record_count = connect.query(f"SELECT COUNT(*) FROM Students WHERE username LIKE '%{searchName}%' AND username != '{username}'")[0][0]
    results = connect.query(f"SELECT * FROM Students WHERE username LIKE '%{searchName}%' AND username != '{username}'")
    print(results)
    dictionary = {}
    dictionary['count'] = record_count

    search_results = []
    for i in range(0, record_count):
        keys = []
        for title in titles:
            if title[0] != 'hashedPassword' and title[0] != 'salt':
                keys.append(title[0])

        values = []
        for entry in results[0]:
            values.append(entry)

        data_dict = dict(zip(keys, values))
        search_results.append(data_dict)

    dictionary['results'] = search_results

    return jsonify(dictionary), 200

@app.route('/degreeinfo', methods=['POST'])
def degreeinfo():
    data = request.get_json()
    if 'username' not in data:
        return jsonify({'error': 'Missing username field'}), 400

    username = data['username']
    count = connect.query(f"SELECT COUNT(*) FROM Students WHERE username = '{username}'")[0][0]
    if count == 0:
        return jsonify({'error': 'Username does not exist'}), 400

    results = connect.query(f"SELECT * FROM Students WHERE username = '{username}'")
    degree_name = results[0][4]
    faculty_name = results[0][3]
    if degree_name == None or faculty_name == None:
        return jsonify({'error': 'No degree declared'}), 400

    requirement_results = connect.query(f"SELECT * FROM Requirements WHERE degreeName = '{degree_name}' AND faculty = '{faculty_name}'")
    requirement_titles = connect.query("SHOW COLUMNS FROM Requirements")
    record_count = connect.query(f"SELECT COUNT(*) FROM Requirements WHERE degreeName = '{degree_name}' AND faculty = '{faculty_name}'")[0][0]
    print(requirement_results)
    dictionary = {}
    dictionary['count'] = record_count

    keys = []
    for j in range(0, len(requirement_titles)-2):
        title = requirement_titles[j]
        keys.append(title[0])

    print(keys)

    results_list = []
    for i in range(0, record_count):
        values = []
        if requirement_results:
            current = requirement_results[i]
            for j in range(0, len(current)-2):
                values.append(current[j])

        data_dict = dict(zip(keys, values))
        results_list.append(data_dict)

    dictionary['results'] = results_list

    return jsonify(dictionary), 200


if __name__ == '__main__':
    app.run(debug=True, port=5001)