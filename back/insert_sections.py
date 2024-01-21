import json
import connect

def generate_insert_queries(section_data):
    insert_queries = []

    for section in section_data:
        dept = section.get('dept')
        course_num = section.get('course_num')
        section_num = section.get('section_num')
        term = section.get('term')
        days = section.get('days')
        start_time, end_time = section.get('time').split('-')

        # Calculate the term value based on the input data
        term_value = f"2023W{term}"

        # Replace 'your_sections_table' with the actual name of your Sections table
        sql_query = f"INSERT INTO Sections (term, section, daysOfWeek, startTime, endTime, courseNum, courseDept) " \
                    f"VALUES ('{term_value}', '{section_num}', '{days}', '{start_time}', '{end_time}', '{course_num}', '{dept}')"

        insert_queries.append(sql_query)

    return insert_queries

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        json_data = json.load(file)
    return json_data

if __name__ == "__main__":
    # Replace 'your_sections_file.json' with the actual path to your JSON file for Sections
    json_file_path = '../data/ubc_courses_data/all_section_list.json'

    # Read JSON data from the file
    json_data = read_json_file(json_file_path)

    # Call the function to generate insert queries
    insert_queries = generate_insert_queries(json_data)

    # Replace 'your_database' with the actual connect object
    for query in insert_queries:
        connect.query(query)
