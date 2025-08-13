from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage
users = {}

# GET all users
@app.route('/users', methods=['GET'])
def get_all_users():
    return jsonify(users)

# POST - add a new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    users[data['id']] = data
    return jsonify({"message": "User added"})

# PUT - update user
@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    if id in users:
        users[id].update(request.json)
        return jsonify({"message": "User updated"})
    return jsonify({"error": "User not found"}), 404

# DELETE - remove user
@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    if id in users:
        del users[id]
        return jsonify({"message": "User deleted"})
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
