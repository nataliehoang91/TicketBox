
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from itsdangerous import URLSafeTimedSerializer


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
app.config['SECRET_KEY'] = "abc"
db = SQLAlchemy(app)





from src.models.event import Event
from src.models.user import User
from src.models.venue import Venue
from src.models.images import Images
from src.models.ticket import Ticket
from src.models.order import Order
from src.models.tickettype import Tickettype
from src.models.type import Type

from flask import  render_template, flash, redirect, url_for,request

from flask_login import UserMixin, LoginManager,login_user,logout_user, current_user, login_required
from flask import request
from flask import session


db.init_app(app)

# token = ts.dumps(User.email, salt='recover-password-secret')

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)



    # blueprint for auth routes in our app
# from .auth import auth as auth_blueprint
# app.register_blueprint(auth_blueprint)

#     # blueprint for non-auth parts of app
# from .main import main as main_blueprint
# app.register_blueprint(main_blueprint)

migrate = Migrate(app, db)

from src.components.events.views import events_blueprint

app.register_blueprint(events_blueprint, url_prefix="/events")

from src.components.account.signup import signup_blueprint
app.register_blueprint(signup_blueprint, url_prefix="/")


