from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

app = Flask(__name__)

# Configure Flask-JWT-Extended
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
jwt = JWTManager(app)

# Dummy user data (replace with your user authentication logic)
users = {
    'user1': {'password': 'password1'},
    'user2': {'password': 'password2'}
}


# Endpoint for user login and token generation
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Replace this with your actual user authentication logic
    if username in users and users[username]['password'] == password:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Invalid username or password"}), 401


# todo: figure out how to implement below function in website
# Protected endpoint that requires a valid token
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = request.jwt_identity
    return jsonify(logged_in_as=current_user), 200

if __name__ == '__main__':
    app.run(debug=True)
