from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user store
users = {}

# ------------------------- GET (Read all users) -------------------------
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200


# ------------------------- GET (Read single user) -------------------------
@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    if user_id in users:
        return jsonify(users[user_id]), 200
    return jsonify({"error": "User not found"}), 404


# ------------------------- POST (Create user) -------------------------
@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    user_id = data.get("id")
    name = data.get("name")

    if not user_id or not name:
        return jsonify({"error": "id and name required"}), 400

    if user_id in users:
        return jsonify({"error": "User already exists"}), 409

    users[user_id] = {"id": user_id, "name": name}
    return jsonify({"message": "User created", "user": users[user_id]}), 201


# ------------------------- PUT (Update user) -------------------------
@app.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.json
    name = data.get("name")

    if not name:
        return jsonify({"error": "name required"}), 400

    users[user_id]["name"] = name
    return jsonify({"message": "User updated", "user": users[user_id]}), 200


# ------------------------- DELETE (Delete user) -------------------------
@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    del users[user_id]
    return jsonify({"message": "User deleted"}), 200


# ------------------------- Run the App -------------------------
if __name__ == "__main__":
    app.run(debug=True)
