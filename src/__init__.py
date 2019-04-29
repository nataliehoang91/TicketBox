
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
POSTGRES = {
   'user': os.environ['PSQL_USER'],
   'pw': os.environ['PSQL_PWD'],
   'db': os.environ['PSQL_DB'],
   'host': os.environ['PSQL_HOST'],
   'port': os.environ['PSQL_PORT'],
}

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:\
%(port)s/%(db)s' % POSTGRES
app.secret_key = "hafha"
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

from src.components.account.signup import signup_blueprint
app.register_blueprint(signup_blueprint, url_prefix="/")


