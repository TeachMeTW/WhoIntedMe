# api.py

from flask import Blueprint, request, jsonify, abort
from .database import db
from .models import User

api = Blueprint("api", __name__)


@api.route("/user", methods=["POST"])
def add_user():
    """
    Add a new user
    ---
    tags:
      - Users
    parameters:
      - name: email
        type: string
        required: true
        description: The email of the user.
      - name: password
        type: string
        required: true
        description: The password for the user.
      - name: first_name
        type: string
        required: true
        description: The first name of the user.
    responses:
      201:
        description: User created successfully
    """
    data = request.get_json()

    # Check if email already exists
    existing_user = User.query.filter_by(email=data["email"]).first()
    if existing_user:
        return jsonify({"message": "User already exists!"}), 400

    new_user = User(
        email=data["email"], password=data["password"], first_name=data["first_name"]
    )
    db.session.add(new_user)
    db.session.commit()

    return (
        jsonify({"message": "User created successfully!", "user_id": new_user.id}),
        201,
    )


@api.route("/user/<int:user_id>/lol-username", methods=["POST"])
def add_lol_username(user_id):
    """
    Add or update a LoL username for a specified user.
    ---
    tags:
      - Users
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: ID of the user for whom the LoL username is to be added
      - name: lol_username
        in: body
        type: string
        required: true
        description: LoL username to be added
    responses:
      200:
        description: LoL username added successfully
      400:
        description: Invalid input or user not found
    """
    user = db.session.get(User, user_id)
    if not user:
        abort(404, description="User not found")
    data = request.get_json()
    if "lol_username" not in data:
        abort(400, description="lol_username not provided")
    user.lol_username = data["lol_username"]
    db.session.commit()
    return jsonify({"message": "LoL username added successfully"})


@api.route("/user/<int:user_id>/lol-username", methods=["PUT"])
def update_lol_username(user_id):
    """
    Update the LoL username for a specified user.
    ---
    tags:
      - Users
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: ID of the user whose LoL username is to be updated
      - name: lol_username
        in: body
        type: string
        required: true
        description: New LoL username to be updated
    responses:
      200:
        description: LoL username updated successfully
      404:
        description: User not found
    """
    user = db.session.get(User, user_id)
    if not user:
        abort(404, description="User not found")
    data = request.get_json()
    user.lol_username = data["lol_username"]
    db.session.commit()
    return jsonify({"message": "LoL username updated successfully"})


@api.route("/user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    """
    Remove a specified user.
    ---
    tags:
      - Users
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: ID of the user to be removed
    responses:
      200:
        description: User removed successfully
      404:
        description: User not found
    """
    user = db.session.get(User, user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully"}), 200


@api.route("/user/<int:user_id>/match-history", methods=["GET"])
def get_match_history(user_id):
    """
    Retrieve the match history for a specified user.
    ---
    tags:
      - Users
    parameters:
      - name: user_id
        in: path
        type: integer
        required: true
        description: ID of the user whose match history is to be retrieved
    responses:
      200:
        description: Match history retrieved successfully
      404:
        description: User not found
    """
    user = db.session.get(User, user_id)
    if not user:
        abort(404, description="User not found")
    # Placeholder match history, replace with actual retrieval logic
    match_history = []
    return jsonify(match_history)
