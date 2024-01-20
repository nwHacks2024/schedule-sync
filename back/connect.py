import pymysql
import config

# Connect to the database
connection = pymysql.connect(
    host=config.host,
    port=config.port,
    user=config.user,
    password=config.password,
    database=config.database  # could also be planner
)

# Create a cursor object
cursor = connection.cursor()

# Execute a SQL query
cursor.execute('SELECT * FROM Degrees')

# Fetch the results
results = cursor.fetchall()

# Print the results
for result in results:
    print(result)

# Close the cursor and connection
cursor.close()
connection.close()