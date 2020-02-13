
from app import db

class User(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    uid=db.Column(db.String(64),unique=True)
    name=db.Column(db.String(120))
    passcode=db.Column(db.String(128))
class Loglist(db.Model):
	id =db.Column(db.Integer, primary_key=True)
	uid=db.Column(db.String(64))
	date=db.Column(db.DateTime)
	location=db.Column(db.String(64))


