from src import db


class Type(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    event_type=db.Column(db.Text, nullable=False)
    events=db.relationship('Event',backref='type', lazy=True)