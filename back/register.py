import bcrypt
import connect

"""
This file contains the functions to register a user with their provided password by hashing it and storing it in the
database. It also contains the function to authenticate a user by comparing the hashed password in the database with the
hashed password provided by the user.
"""


# Function to register a new user in the database
def register_user(username, password, firstName, lastName):
    # Generate a random salt using bcrypt
    salt = bcrypt.gensalt()
    # Hash the password using the generated salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    # Convert the salt and hashed password to strings for database storage
    salt_str = salt.decode('utf-8')
    hashed_password_str = hashed_password.decode('utf-8')

    query_string = (f"INSERT INTO Students VALUES('{username}',"
                    + (f" '{firstName}'," if firstName else " NULL,")
                    + (f" '{lastName}'," if lastName else " NULL,")
                    + f" 'Science', 'Computer Science', '{hashed_password_str}', '{salt_str}')")

    # Execute the SQL query to register the user in the database
    connect.query(query_string)

# Function to authenticate a user during login
def authenticate_user(username, password):
    query_string = f"SELECT salt, hashedPassword FROM Students WHERE username = '{username}'"
    results = connect.query(query_string)

    # Check if the username exists in the database
    if len(results) == 0:
        return False

    # Retrieve the salt and hashed password from the query results
    salt = results[0][0].encode('utf-8')
    hashed_password = results[0][1].encode('utf-8')

    # Check if the hashed password matches the input password after hashing with the stored salt
    if bcrypt.hashpw(password.encode('utf-8'), salt) == hashed_password:
        return True
    else:
        return False