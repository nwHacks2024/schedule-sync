import pymysql

# Set the database credentials
host = 'bdec.cjumg64mkato.us-east-1.rds.amazonaws.com'
port = 3306
user = 'admin'
password = 'nwhacks2024'
database = 'planner'

# Connect to the database
connection = pymysql.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=database  # could also be planner
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