"""
This file contains the API endpoints for the application. The endpoints are used to interact with the database and perform
various operations such as user registration, login, course enrollment, and friend management. The endpoints are used to
fetch and update data in the database and return the results in JSON format.
"""

from datetime import datetime, timedelta
from flask import Flask, request, jsonify
import connect
import register as reg

app = Flask(__name__)


@app.route('/api/userprofile', methods=['GET'])
def userinfo():
    titles = connect.query("SHOW COLUMNS FROM Students")

    username = request.args.get('username')

    if username is None:
        return jsonify({'error': 'Missing username field'}), 400

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


@app.route('/api/friends', methods=['GET'])
def friends():
    friend_titles = connect.query("SHOW COLUMNS FROM Friends")

    username = request.args.get('username')

    if username is None:
        return jsonify({'error': 'Missing username field'}), 400

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


def repeat_events(start_date, days_of_week, max_repeats):
    repeats = 0
    current_date = start_date

    while repeats < max_repeats:
        # Check if the current day of the week matches any specified days
        if current_date.strftime('%a') in days_of_week:
            # Yield the date without the time portion
            yield current_date.strftime('%Y-%m-%d')

            repeats += 1

        # Move to the next day based on the specific days mentioned
        if 'Mon' in days_of_week:
            current_date += timedelta(days=1)
        elif 'Tue' in days_of_week:
            current_date += timedelta(days=1)
        elif 'Wed' in days_of_week:
            current_date += timedelta(days=1)
        elif 'Thu' in days_of_week:
            current_date += timedelta(days=1)
        elif 'Fri' in days_of_week:
            current_date += timedelta(days=1)


@app.route('/api/registeredcourses', methods=['GET'])
def registeredcourses():
    username = request.args.get('username')

    if username is None:
        return jsonify({'error': 'Missing username field'}), 400

    term = '2023W2'  # Adjust the term as needed

    # Query to fetch enrolled courses for a specific term
    sql_query = f"""
    SELECT
        Sections.term,
        Sections.section,
        Sections.courseNum,
        Sections.courseDept,
        Sections.daysOfWeek,
        Sections.startTime,
        Sections.endTime
    FROM
        Sections
    INNER JOIN
        Enrolled ON Sections.term = Enrolled.term
                  AND Sections.section = Enrolled.section
                  AND Sections.courseNum = Enrolled.courseNum
                  AND Sections.courseDept = Enrolled.courseDept
    WHERE
        Enrolled.username = '{username}' AND Sections.term = '{term}';
    """

    results = connect.query(sql_query)

    if not results:
        response_dict = {
            'count': 0,
            'results': []
        }
        return jsonify(response_dict), 200

    # Define the keys for the JSON response
    keys = ['term', 'section', 'courseNum', 'courseDept', 'daysOfWeek', 'startTime', 'endTime']

    # Create a list of dictionaries for each course
    all_enrollments = [dict(zip(keys, course)) for course in results]

    # Combine courseDept and courseNum into courseName
    for course in all_enrollments:
        course['courseName'] = f"{course['courseDept']} {course['courseNum']}"
        del course['courseDept']
        del course['courseNum']

        # Generate repeated events based on days of the week
        start_date = datetime.strptime('2024-01-15', '%Y-%m-%d')
        days_of_week = course['daysOfWeek']
        max_repeats = 10
        course['events'] = list(repeat_events(start_date, days_of_week, max_repeats))

    # Create the final response dictionary
    response_dict = {
        'count': len(all_enrollments),
        'results': all_enrollments
    }

    return jsonify(response_dict)


@app.route('/api/login', methods=['GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    if username is None:
        return jsonify({'error': 'Missing username field'}), 400
    if password is None:
        return jsonify({'error': 'Missing password field'}), 400

    count = connect.query(f"SELECT COUNT(*) FROM Students WHERE username = '{username}'")[0][0]
    if count == 0:
        return jsonify({'error': 'Username does not exist'}), 400

    if reg.authenticate_user(username, password):
        return jsonify({'success': 'Login successful'}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401


@app.route('/api/users', methods=['GET'])
def users():

    username = request.args.get('username')
    search_name = request.args.get('searchName')

    if username is None:
        return jsonify({'error': 'Missing username field'}), 400
    if search_name is None:
        return jsonify({'error': 'Missing searchName field'}), 400

    titles = connect.query("SHOW COLUMNS FROM Students")

    count = connect.query(f"SELECT COUNT(*) FROM Students WHERE username = '{username}'")[0][0]
    if count == 0:
        return jsonify({'error': 'Username does not exist'}), 400

    record_count = connect.query(f"SELECT COUNT(*) FROM Students WHERE username LIKE '%{search_name}%' AND username != '{username}'")[0][0]
    results = connect.query(f"SELECT * FROM Students WHERE username LIKE '%{search_name}%' AND username != '{username}'")

    dictionary = {}
    dictionary['count'] = record_count

    search_results = []
    keys = []
    for title in titles:
        if title[0] != 'hashedPassword' and title[0] != 'salt':
            keys.append(title[0])
    for i in range(0, record_count):
        values = []
        for entry in results[i]:
            values.append(entry)

        data_dict = dict(zip(keys, values))
        search_results.append(data_dict)

    dictionary['results'] = search_results

    return jsonify(dictionary), 200


@app.route('/api/degreeinfo', methods=['GET'])
def degreeinfo():
    username = request.args.get('username')

    if username is None:
        return jsonify({'error': 'Missing username field'}), 400

    count = connect.query(f"SELECT COUNT(*) FROM Students WHERE username = '{username}'")[0][0]
    if count == 0:
        return jsonify({'error': 'Username does not exist'}), 400

    results = connect.query(f"SELECT * FROM Students WHERE username = '{username}'")
    degree_name = results[0][4]
    faculty_name = results[0][3]

    if degree_name is None or faculty_name is None:
        return jsonify({'error': 'No degree declared'}), 400

    requirement_results = connect.query(f"SELECT * FROM Requirements WHERE degreeName = '{degree_name}' AND faculty = '{faculty_name}'")
    requirement_titles = connect.query("SHOW COLUMNS FROM Requirements")
    record_count = connect.query(f"SELECT COUNT(*) FROM Requirements WHERE degreeName = '{degree_name}' AND faculty = '{faculty_name}'")[0][0]

    dictionary = {}
    dictionary['count'] = record_count

    keys = []
    for j in range(0, len(requirement_titles)-2):
        title = requirement_titles[j]
        keys.append(title[0])

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


@app.route('/api/courses', methods=['GET'])
def courses():
    department = request.args.get('department')

    if department is None:
        return jsonify({'error': 'Missing department field'}), 400

    count = connect.query(f"SELECT COUNT(*) FROM Courses WHERE dept = '{department}'")[0][0]
    if count == 0:
        return jsonify({'error': 'Department does not exist'}), 400

    record_count = connect.query(f"SELECT COUNT(*) FROM Courses WHERE dept = '{department}'")[0][0]
    results = connect.query(f"SELECT * FROM Courses WHERE dept = '{department}'")

    titles = connect.query("SHOW COLUMNS FROM Courses")

    dictionary = {}
    dictionary['count'] = record_count

    search_results = []

    keys = []
    for title in titles:
        keys.append(title[0])

    for i in range(0, record_count):
        values = []
        for entry in results[i]:
            values.append(entry)

        data_dict = dict(zip(keys, values))
        search_results.append(data_dict)

    dictionary['results'] = search_results

    return jsonify(dictionary), 200


@app.route('/api/sections', methods=['GET'])
def sections():
    course_num = request.args.get('courseNum')
    course_dept = request.args.get('courseDept')

    if course_num is None:
        return jsonify({'error': 'Missing courseNum field'}), 400
    if course_dept is None:
        return jsonify({'error': 'Missing courseDept field'}), 400

    count = connect.query(f"SELECT COUNT(*) FROM Courses WHERE courseNum = '{course_num}' AND dept = '{course_dept}'")[0][0]
    if count == 0:
        return jsonify({'error': 'Course does not exist'}), 400

    record_count = connect.query(f"SELECT COUNT(*) FROM Sections WHERE courseNum = '{course_num}' AND courseDept = '{course_dept}'")[0][0]
    results = connect.query(f"SELECT * FROM Sections WHERE courseNum = '{course_num}' AND courseDept = '{course_dept}'")

    titles = connect.query("SHOW COLUMNS FROM Sections")

    dictionary = {}
    dictionary['count'] = record_count

    search_results = []

    keys = []
    for title in titles:
        keys.append(title[0])

    for i in range(0, record_count):
        values = []
        for entry in results[i]:
            values.append(entry)

        data_dict = dict(zip(keys, values))
        search_results.append(data_dict)

    dictionary['results'] = search_results

    return jsonify(dictionary), 200


@app.route('/api/sectioninfo', methods=['GET'])
def sectioninfo():
    course_num = request.args.get('courseNum')
    course_dept = request.args.get('courseDept')
    section_num = request.args.get('sectionNum')

    if course_num is None:
        return jsonify({'error': 'Missing courseNum field'}), 400
    if course_dept is None:
        return jsonify({'error': 'Missing courseDept field'}), 400
    if section_num is None:
        return jsonify({'error': 'Missing sectionNum field'}), 400

    term = "2023W2"
    count = connect.query(f"SELECT COUNT(*) FROM Courses WHERE courseNum = '{course_num}' AND dept = '{course_dept}'")[0][0]
    if count == 0:
        return jsonify({'error': 'Course does not exist'}), 400

    sql_query = f"""
SELECT
    Teaches.profName,
    Teaches.profDept,
    Sections.term,
    Sections.section,
    Sections.daysOfWeek,
    Sections.startTime,
    Sections.endTime,
    Sections.courseNum,
    Sections.courseDept
FROM
    Teaches
RIGHT OUTER JOIN
    Sections ON Teaches.term = Sections.term
              AND Teaches.section = Sections.section
              AND Teaches.courseNum = Sections.courseNum
              AND Teaches.courseDept = Sections.courseDept
WHERE
    Sections.courseNum = '{course_num}'
    AND Sections.courseDept = '{course_dept}'
    AND Sections.section = '{section_num}'
    AND Sections.term = '{term}';
"""

    results = connect.query(sql_query)

    section_titles = connect.query("SHOW COLUMNS FROM Sections")
    prof_titles = connect.query("SHOW COLUMNS FROM Professors")

    keys = []
    for i in range(0, len(prof_titles)-3):
        title = prof_titles[i]
        keys.append(title[0])
    for title in section_titles:
         keys.append(title[0])

    values = []
    for entry in results[0]:
         values.append(entry)

    data_dict = dict(zip(keys, values))

    return jsonify(data_dict), 200


@app.route('/api/removecourse', methods=['DELETE'])
def removecourse():
    username = request.args.get('username')
    section = request.args.get('section')
    course_num = request.args.get('courseNum')
    course_dept = request.args.get('courseDept')

    if username is None:
        return jsonify({'error': 'Missing username field'}), 400
    if section is None:
        return jsonify({'error': 'Missing section field'}), 400
    if course_num is None:
        return jsonify({'error': 'Missing courseNum field'}), 400
    if course_dept is None:
        return jsonify({'error': 'Missing courseDept field'}), 400

    term = "2023W2"
    try:
        connect.query(f"DELETE FROM Enrolled WHERE username='{username}' AND term='{term}' AND section='{section}' AND courseNum='{course_num}' AND courseDept='{course_dept}'")
        return jsonify({'success': 'Course section deleted!'}), 200
    except:
        return jsonify({'error': 'Invalid course deletion'}), 400


@app.route('/api/removefriend', methods=['DELETE'])
def removefriend():
    username = request.args.get('username')
    friend_username = request.args.get('friendUsername')

    if username is None:
        return jsonify({'error': 'Missing username field'}), 400
    if friend_username is None:
        return jsonify({'error': 'Missing friendUsername field'}), 400

    try:
        connect.query(f"DELETE FROM Friends WHERE username='{username}' AND friendUsername='{friend_username}'")
        connect.query(f"DELETE FROM Friends WHERE username='{friend_username}' AND friendUsername='{username}'")
        return jsonify({'success': 'Friend removed'}), 200
    except:
        return jsonify({'error': 'Could not remove friend'}), 400


@app.route('/api/addcourse', methods=['POST'])
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

    section = data['section']
    term = "2023W2"

    section = str(section)

    if (section[0] == '1' or section[1] == '1'):
        term = "2023W1"

    try:
        connect.query(f"INSERT INTO Enrolled VALUES ('{data['username']}', '{term}', '{data['section']}', '{data['courseNum']}', '{data['courseDept']}')")
        return jsonify({'success': 'Course section added'}), 200
    except:
        return jsonify({'error': 'Invalid course addition'}), 400


@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json() #json body
    first_name = ""
    last_name = ""
    if 'username' not in data:
        return jsonify({'error': 'Missing username field'}), 400
    elif 'password' not in data:
        return jsonify({'error': 'Missing password field'}), 400

    if 'firstName' in data:
        first_name = data['firstName']
    if 'lastName' in data:
        last_name = data['lastName']

    try:
        reg.register_user(data['username'], data['password'], f'{first_name}', f'{last_name}')
        return jsonify({'success': 'User registered'}), 200
    except Exception as e:
        print(e)
        return jsonify({'error': 'Could not register user'}), 400


@app.route('/api/addfriend', methods=['POST'])
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