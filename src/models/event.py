
from src import db

class Event(db.Model):

    __tablename__ = 'event'

    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String,nullable=False)
    description = db.Column(db.Text, nullable=False)
    start_time=db.Column(db.DateTime)
    end_time=db.Column(db.DateTime)
    organizer_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'),
        nullable=False)
    eventtype_id=db.Column(db.Integer, db.ForeignKey('type.id'),
        nullable=False)
    