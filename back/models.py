from .database import db

from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(150), nullable=True)
    lol_username = db.Column(db.String(150), default="None", nullable=True)
    matches = db.relationship("Match", backref="user", lazy=True)


class Match(db.Model):
    __tablename__ = "match"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    gameCreation = db.Column(db.Integer, nullable=False)
    gameDuration = db.Column(db.Integer, nullable=False)
    gameMode = db.Column(db.String(50), nullable=True)
    players = db.relationship("PlayerMatchStats", backref="match", lazy=True)


class PlayerMatchStats(db.Model):
    __tablename__ = "player_match_stats"

    id = db.Column(db.Integer, primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey("match.id"), nullable=False)
    summonerName = db.Column(db.String(255), nullable=True)
    win = db.Column(db.Boolean, nullable=True)
    teamId = db.Column(db.Integer, nullable=True)
    teamPosition = db.Column(db.String(50), nullable=True)
    role = db.Column(db.String(50), nullable=True)
    kills = db.Column(db.Integer, nullable=True)
    deaths = db.Column(db.Integer, nullable=True)
    assists = db.Column(db.Integer, nullable=True)
    goldEarned = db.Column(db.Integer, nullable=True)
    totalDamageDealt = db.Column(db.Integer, nullable=True)
    totalDamageTaken = db.Column(db.Integer, nullable=True)
    visionScore = db.Column(db.Integer, nullable=True)
    wardsPlaced = db.Column(db.Integer, nullable=True)
    wardsKilled = db.Column(db.Integer, nullable=True)
    totalMinionsKilled = db.Column(db.Integer, nullable=True)
    turretKills = db.Column(db.Integer, nullable=True)
    totalTimeSpentDead = db.Column(db.Integer, nullable=True)
    puuid = db.Column(db.String(255), nullable=True)
    champLevel = db.Column(db.Integer, nullable=True)
    championName = db.Column(db.String(100), nullable=True)
    lane = db.Column(db.String(50), nullable=True)
    totalHealsOnTeammate = db.Column(db.Integer, nullable=True)
    baitPings = db.Column(db.Integer, nullable=True)
