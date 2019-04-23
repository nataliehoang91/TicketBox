from src import db


class Images(db.model):

    __tablename__=images
    
    id = db.Column(db.Integer, primary_key=True)
    event_id=db.Column(db.Integer)
    image_url=db.Column(db.String)