from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user storage (acts like a mini database)
users = {}

# --------------------
# ROUTES
# --------------------

# 1. GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200


# 2. GET a single user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[user_id]), 200


# 3. POST - Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Name and email are required"}), 400

    new_id = len(users) + 1
    users[new_id] = {
        "id": new_id,
        "name": data["name"],
        "email": data["email"]
    }

    return jsonify(users[new_id]), 201


# 4. PUT - Update a user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.json
    users[user_id]["name"] = data.get("name", users[user_id]["name"])
    users[user_id]["email"] = data.get("email", users[user_id]["email"])

    return jsonify(users[user_id]), 200


# 5. DELETE - Remove a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    deleted = users.pop(user_id)
    return jsonify({"message": "User deleted", "user": deleted}), 200


# Run server
if __name__ == '__main__':
    app.run(debug=True)
