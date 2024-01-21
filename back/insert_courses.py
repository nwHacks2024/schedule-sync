import json
import connect


def generate_insert_queries(course_data):
    insert_queries = []

    for course in course_data:
        course_num = course.get('courseNum')
        dept = course.get('dept')

        # Replace 'your_table' with the actual name of your table
        sql_query = f"INSERT INTO Courses (courseNum, dept) VALUES ('{course_num}', '{dept}')"

        insert_queries.append(sql_query)

    return insert_queries

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        json_data = json.load(file)
    return json_data

if __name__ == "__main__":
    # Replace 'your_file.json' with the actual path to your JSON file
    json_file_path = '../data/ubc_dept_data/CPSC.json'

    # Read JSON data from the file
    json_data = read_json_file(json_file_path)

    # Call the function to generate insert queries
    insert_queries = generate_insert_queries(json_data)

    # Replace 'your_database' with the actual connect object
    for query in insert_queries:
        try:
            connect.query(query)
        except:
            pass
