
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

from src.models.event import Event
from src.models.user import User
from src.model.venue import Venue
from src.model.images import Images

migrate = Migrate(app, db)

# from src.components.events.views import events_blueprint
# app.register_blueprint(events_blueprint, url_prefix="/events")
