
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../test.db'
app.secret_key = "VA xau xi haha"
db = SQLAlchemy(app)

from src.models.event import Event
from src.models.user import User
from src.models.venue import Venue
from src.models.images import Images
from src.models.ticket import Ticket
from src.models.order import Order
from src.models.tickettype import Tickettype
from src.models.type import Type


migrate = Migrate(app, db)

from src.components.events.views import events_blueprint

app.register_blueprint(events_blueprint, url_prefix="/events")
