from flask import Blueprint, render_template
from src import db


events_blueprint=Blueprint('events',__name__,template_folder='../../templates/events')


from src.components.events.forms import AddEventForm
from src.models.user import User
from src.models.event import Event
from src.models.venue import Venue

@events_blueprint.route('/')
def hello():
    return render_template('events.html')

@events_blueprint.route('/add',methods=['POST','GET'])

def add():
    form=AddEventForm()
    form.venue.choices=[(u.id,u.venue_name) for u in Venue.query.all()]
    form.organizer.choices=[(u.id,u.username) for u in User.query.all()]
    if form.validate_on_submit():
        e=Event(venue_id=form.venue.data,description=form.description.data,organizer_id=form.organizer.data)
        db.session.add(e)
        db.session.commit()
    return render_template('add_event.html',form=form)

@events_blueprint.route('/list')
def list():
    return "Here all Events"