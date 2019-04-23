from src import db

class Venue(db.Model):

    __tablenameç__="venue"
    
    id=db.Column(db.Integer, primary_key=True)
    venue_name=db.Column(db.String, nullable=False)
    location=db.Column(db.String, nullable=False)
    events = db.relationship('Event', backref='venue', lazy=True)

  