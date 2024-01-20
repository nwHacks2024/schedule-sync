import pymysql

# Set the database credentials
host = '<YOUR_RDS_ENDPOINT>'
port = 3306
user = '<YOUR_DATABASE_USERNAME>'
password = '<YOUR_DATABASE_PASSWORD>'
database = '<YOUR_DATABASE_NAME>'

# Connect to the database
connection = pymysql.connect(
    host="bdec.cjumg64mkato.us-east-1.rds.amazonaws.com",
    port=3306,
    user="nwhacks2024",
    password="nwhacks2024",
    database="bdec"  # could also be planner
)

# Create a cursor object
# cursor = connection.cursor()
#
# # Execute a SQL query
# cursor.execute('SELECT * FROM users')
#
# # Fetch the results
# results = cursor.fetchall()
#
# # Print the results
# for result in results:
#     print(result)
#
# # Close the cursor and connection
# cursor.close()
connection.close()