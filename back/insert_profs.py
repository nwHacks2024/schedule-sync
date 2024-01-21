import json
import connect

def generate_insert_queries(prof_data):
    insert_queries = []

    for professor in prof_data:
        prof_name = professor.get('name') if professor.get('name') != "NA" else "NULL"
        avg_rating = professor.get('avgRating') if professor.get('avgRating') != "NA" else "NULL"
        avg_difficulty = professor.get('avgDifficulty') if professor.get('avgDifficulty') != "NA" else "NULL"
        num_ratings = professor.get('numRatings') if professor.get('numRatings') != "NA" else "NULL"
        prof_name = prof_name.title()
        # Replace 'your_table' with the actual name of your Professors table
        if (prof_name != "NULL"):
            sql_query = f"INSERT INTO Professors (profName, profDept, avgRating, avgDifficulty, numRatings) " \
                        f"VALUES ('{prof_name}', 'Computer Science', {avg_rating}, {avg_difficulty}, {num_ratings})"
        else:
            sql_query = f"INSERT INTO Professors (profName, profDept, avgRating, avgDifficulty, numRatings) " \
                        f"VALUES (NULL, 'Computer Science', {avg_rating}, {avg_difficulty}, {num_ratings})"

        insert_queries.append(sql_query)

    return insert_queries

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        json_data = json.load(file)
    return json_data

if __name__ == "__main__":
    # Replace 'your_professors_file.json' with the actual path to your JSON file for Professors
    json_file_path = '../data/rate_my_prof_data/all_prof_list.json'

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
