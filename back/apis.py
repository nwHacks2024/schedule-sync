import json
from datetime import datetime, timedelta
from flask import Flask, request, jsonify
import connect
import register

app = Flask(__name__)


@app.route('/api/userprofile', methods=['POST'])
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

@app.route('/api/friends', methods=['POST'])
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

# @app.route('/api/registeredcourses', methods=['POST'])
# def registeredcourses():
#     data = request.get_json() #json body

#     if 'username' not in data:
#         return jsonify({'error': 'Missing username field'}), 400

#     username = data['username']

#     enrolled_titles = connect.query("SHOW COLUMNS FROM Enrolled")
#     section_titles = connect.query("SHOW COLUMNS FROM Sections")

#     count = connect.query(f"SELECT COUNT(*) FROM Students WHERE username = '{username}'")[0][0]
#     if count == 0:
#         return jsonify({'error': 'Username does not exist'}), 400

#     record_count = connect.query(f"SELECT COUNT(*) FROM Enrolled WHERE username = '{username}'")[0][0]

#     dictionary = {}
#     dictionary['count'] = record_count

#     results = connect.query(f"SELECT * FROM Enrolled WHERE username = '{username}' AND Term = '2023W2'")
#     sql_query = f"""
#     SELECT
#     Sections.term,
#     Sections.section,
#     Sections.courseNum,
#     Sections.courseDept,
#     Sections.daysOfWeek,
#     Sections.startTime,
#     Sections.endTime
# FROM
#     Sections
# INNER JOIN
#     Enrolled ON Sections.term = Enrolled.term
#               AND Sections.section = Enrolled.section
#               AND Sections.courseNum = Enrolled.courseNum
#               AND Sections.courseDept = Enrolled.courseDept
#     WHERE Enrolled.username = '{username}' AND Sections.term = '2023W2';
#     """

#     results = connect.query(sql_query)

#     keys = []
#     for j in range(1, len(enrolled_titles)):
#          title = enrolled_titles[j]
#          keys.append(title[0])
#     for j in range(len(section_titles)):
#         title = section_titles[j]
#         if (not keys.__contains__(title[0])):
#             keys.append(title[0])

#     all_enrollments = []

#     for i in range(0, record_count):
#         values = []
#         if results:
#             current = results[i]
#             for j in range(1, len(current)):
#                 values.append(current[j])

#         data_dict = dict(zip(keys, values))
#         all_enrollments.append(data_dict)

#     dictionary['results'] = all_enrollments

#     # Convert the dictionary to a JSON-formatted string
#     return jsonify(dictionary)
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

@app.route('/api/registeredcourses', methods=['POST'])
def registeredcourses():
    data = request.get_json()

    if 'username' not in data:
        return jsonify({'error': 'Missing username field'}), 400

    username = data['username']
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
        return jsonify({'error': 'No courses found for the given username and term'}), 404

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

@app.route('/api/courses', methods=['POST'])
def courses():
    data = request.get_json()
    if 'department' not in data:
        return jsonify({'error': 'Missing department field'}), 400

    department = data['department']
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

@app.route('/sections', methods=['POST'])
def sections():
    data = request.get_json()
    if 'courseNum' not in data:
        return jsonify({'error': 'Missing courseNum field'}), 400
    if 'courseDept' not in data:
        return jsonify({'error': 'Missing courseDept field'}), 400

    courseNum = data['courseNum']
    courseDept = data['courseDept']
    count = connect.query(f"SELECT COUNT(*) FROM Courses WHERE courseNum = '{courseNum}' AND dept = '{courseDept}'")[0][0]
    if count == 0:
        return jsonify({'error': 'Course does not exist'}), 400

    record_count = connect.query(f"SELECT COUNT(*) FROM Sections WHERE courseNum = '{courseNum}' AND courseDept = '{courseDept}'")[0][0]
    results = connect.query(f"SELECT * FROM Sections WHERE courseNum = '{courseNum}' AND courseDept = '{courseDept}'")

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


@app.route('/sectioninfo', methods=['POST'])
def sectioninfo():
    data = request.get_json()
    if 'courseNum' not in data:
        return jsonify({'error': 'Missing courseNum field'}), 400
    if 'courseDept' not in data:
        return jsonify({'error': 'Missing courseDept field'}), 400
    if 'sectionNum' not in data:
        return jsonify({'error': 'Missing sectionNum field'}), 400

    courseNum = data['courseNum']
    courseDept = data['courseDept']
    sectionNum = data['sectionNum']
    term = "2023W2"
    count = connect.query(f"SELECT COUNT(*) FROM Courses WHERE courseNum = '{courseNum}' AND dept = '{courseDept}'")[0][0]
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
INNER JOIN
    Sections ON Teaches.term = Sections.term
              AND Teaches.section = Sections.section
              AND Teaches.courseNum = Sections.courseNum
              AND Teaches.courseDept = Sections.courseDept
WHERE
    Sections.courseNum = '{courseNum}'
    AND Sections.courseDept = '{courseDept}'
    AND Sections.section = '{sectionNum}'
    AND Sections.term = '{term}';
"""

    results = connect.query(sql_query)

    section_titles = connect.query("SHOW COLUMNS FROM Sections")
    prof_titles = connect.query("SHOW COLUMNS FROM Professors")

    data_dict = {}

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
        register.register_user(data['username'], data['password'], f'{first_name}', f'{last_name}')
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