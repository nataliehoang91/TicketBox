
from src import db

class Event(db.Model):

    __tablename__ = 'event'

    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'),
        nullable=False)
    description = db.Column(db.Text, nullable=False)
    organizer_id = db.Column(db.Integer, db.ForeignKey('organizer.id'),
        nullable=False)
    end_time = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

