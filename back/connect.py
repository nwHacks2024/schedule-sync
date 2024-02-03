import pymysql
import config

"""
This file contains the functions to connect to the database and run a SQL query in the database.
"""

# Connect to database and run sql query in database
def query(sql_query: str):
    # Connect to the database
    connection = pymysql.connect(
        host=config.host,
        port=config.port,
        user=config.user,
        password=config.password,
        database=config.database
    )

    # Create a cursor object
    cursor = connection.cursor()

    # Execute a SQL query
    cursor.execute(sql_query)

    # Fetch the results
    results = cursor.fetchall()
    connection.commit()

    # Close the cursor and connection
    cursor.close()
    connection.close()

    return results
