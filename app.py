from flask import Flask, request, jsonify
from flask_cors import CORS # type: ignore

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/', methods=['POST'])
def login():
    # Get form data safely
    username = request.form.get('username')
    password = request.form.get('password')

    # Check if both values are provided
    if not username or not password:
        return jsonify({'status': 'fail', 'message': 'Missing username or password'}), 400

    # Dummy authentication logic
    if username == 'admin' and password == 'password':
        return jsonify({'status': 'success', 'message': 'Login successful'})
    else:
        return jsonify({'status': 'fail', 'message': 'Invalid credentials'}), 401

# Run the app
if __name__ == '_main_':
    app.run(debug=True)