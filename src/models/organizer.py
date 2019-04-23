from src import db

class Organizer(db.Model):

  __tablename__ = 'organizer'

  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(120), index=True, unique=True)
  password_hash = db.Column(db.String(128), nullable=False)
  events = db.relationship('Event', backref='organizer', lazy=True)
  