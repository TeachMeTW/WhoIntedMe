# api.py

from flask import Blueprint, request, jsonify, abort
from .database import db
from .riot_api import get_all_matches
from .models import User, Match, PlayerMatchStats

api = Blueprint("api", __name__)


@api.route("/user", methods=["POST"])
def add_user():
    """
    Add a new user
    ---
    tags:
      - Users
    consumes:
      - application/json
    produces:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            email:
              type: string
              description: The email of the user.
            password:
              type: string
              description: The password for the user.
            first_name:
              type: string
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
    consumes:
      - application/json
    produces:
      - application/json
    parameters:
      - in: path
        name: user_id
        type: integer
        required: true
        description: ID of the user for whom the LoL username is to be added
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            lol_username:
              type: string
              description: LoL username to be added
    responses:
      200:
        description: LoL username added successfully
      400:
        description: Invalid input or user not found
    """
    user = db.session.get(User, user_id)
    print(request.data)
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
    consumes:
      - application/json
    produces:
      - application/json
    parameters:
      - in: path
        name: user_id
        type: integer
        required: true
        description: ID of the user whose LoL username is to be updated
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            lol_username:
              type: string
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
        abort(404, description="User not found")
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully"})


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
    user = User.query.get(user_id)
    if not user:
        abort(404, description="User not found")

    # Fetch match history using the provided riot_api.py functions
    all_matches = get_all_matches(user.lol_username)

    # Store matches in database
    for match_data in all_matches:

        match = Match.query.filter_by(id=match_data["gameId"]).first()
        print(match)
        if not match:
            new_match = Match(
                id=match_data["gameId"],
                gameCreation=match_data["gameCreation"],
                gameDuration=match_data["gameDuration"],
                gameMode=match_data["gameMode"],
            )

            for player_data in match_data.get("participants", []):
                print(player_data)
                player_stats = PlayerMatchStats(
                    summonerName=player_data.get("summonerName"),
                    win=player_data.get("win"),
                    teamId=player_data.get("teamId"),
                    teamPosition=player_data.get("teamPosition"),
                    role=player_data.get("role"),
                    kills=player_data.get("kills"),
                    deaths=player_data.get("deaths"),
                    assists=player_data.get("assists"),
                    goldEarned=player_data.get("goldEarned"),
                    totalDamageDealt=player_data.get("totalDamageDealt"),
                    totalDamageTaken=player_data.get("totalDamageTaken"),
                    visionScore=player_data.get("visionScore"),
                    wardsPlaced=player_data.get("wardsPlaced"),
                    wardsKilled=player_data.get("wardsKilled"),
                    totalMinionsKilled=player_data.get("totalMinionsKilled"),
                    turretKills=player_data.get("turretKills"),
                    totalTimeSpentDead=player_data.get("totalTimeSpentDead"),
                    puuid=player_data.get("puuid"),
                    champLevel=player_data.get("champLevel"),
                    championName=player_data.get("championName"),
                    lane=player_data.get("lane"),
                    totalHealsOnTeammate=player_data.get("totalHealsOnTeammate"),
                    baitPings=player_data.get("baitPings"),
                )

                new_match.players.append(player_stats)

            user.matches.append(new_match)
            db.session.add(new_match)

    db.session.commit()

    # Return match history from database
    match_history = [
        {
            "id": match.id,
            "gameCreation": match.gameCreation,
            "gameDuration": match.gameDuration,
            "gameMode": match.gameMode,
            "players": [
                {
                    "summonerName": player.summonerName,
                }
                for player in match.players
            ],
        }
        for match in user.matches
    ]

    return jsonify(match_history)
