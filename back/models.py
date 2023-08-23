from .database import db

from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    lol_username = db.Column(db.String(150), default="None")
    # relationship with Match model
    matches = db.relationship("Match", backref="user", lazy=True)


class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gameCreation = db.Column(db.Integer)
    gameDuration = db.Column(db.Integer)
    gameMode = db.Column(db.String(50))
    players = db.relationship("PlayerMatchStats", backref="match", lazy=True)


class PlayerMatchStats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey("match.id"), nullable=False)
    summonerName = db.Column(db.String(255))
    win = db.Column(db.Boolean)
    teamId = db.Column(db.Integer)
    teamPosition = db.Column(db.String(50))
    role = db.Column(db.String(50))
    kills = db.Column(db.Integer)
    deaths = db.Column(db.Integer)
    assists = db.Column(db.Integer)
    goldEarned = db.Column(db.Integer)
    totalDamageDealt = db.Column(db.Integer)
    totalDamageTaken = db.Column(db.Integer)
    visionScore = db.Column(db.Integer)
    wardsPlaced = db.Column(db.Integer)
    wardsKilled = db.Column(db.Integer)
    totalMinionsKilled = db.Column(db.Integer)
    turretKills = db.Column(db.Integer)
    totalTimeSpentDead = db.Column(db.Integer)
    puuid = db.Column(db.String(255))
    champLevel = db.Column(db.Integer)
    championName = db.Column(db.String(100))
    lane = db.Column(db.String(50))
    totalHealsOnTeammate = db.Column(db.Integer, nullable=True)
    baitPings = db.Column(db.Integer)
