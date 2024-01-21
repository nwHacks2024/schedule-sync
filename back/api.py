from flask import Flask
import connect

app = Flask(__name__)


@app.route('/api/users', methods=['GET'])
def hello():
    results = connect.query("SELECT * FROM Students")
    return {'message': 'Hello, World!'}

if __name__ == '__main__':
    app.run(debug=True)