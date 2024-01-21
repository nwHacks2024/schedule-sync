import bcrypt
import connect


def register_user(username, password, firstName, lastName):
    # Generate a random salt
    salt = bcrypt.gensalt()
    # Hash the password with the salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    salt_str = salt.decode('utf-8')
    hashed_password_str = hashed_password.decode('utf-8')

    query_string = (f"INSERT INTO Students VALUES('{username}',"
                    + (f" '{firstName}'," if firstName else " NULL,")
                    + (f" '{lastName}'," if lastName else " NULL,")
                    + f" NULL, NULL, '{hashed_password_str}', '{salt_str}')")
    print(query_string)

    print(connect.query(query_string))

def authenticate_user(username, password):
    query_string = f"SELECT salt, hashedPassword FROM Students WHERE username = '{username}'"
    print(query_string)
    results = connect.query(query_string)
    if len(results) == 0:
        return False
    salt = results[0][0].encode('utf-8')
    hashed_password = results[0][1].encode('utf-8')
    if bcrypt.hashpw(password.encode('utf-8'), salt) == hashed_password:
        return True
    else:
        return False