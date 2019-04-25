from flask import Blueprint, render_template,request
from src import db


events_blueprint=Blueprint('events',__name__,template_folder='../../templates/events')


from src.components.events.forms import AddEventForm
from src.models.user import User
from src.models.event import Event
from src.models.venue import Venue
from src.models.type import Type

@events_blueprint.route('/')
def hello():
    return render_template('events.html')

@events_blueprint.route('/add',methods=['POST','GET'])
def add():
    form=AddEventForm()
    print('****** mothefugqueereiofwj')
    print(form)

    form.eventtype.choices=[(t.id,t.event_type) for t in Type.query.all()]
    if request.method == 'POST':
        v=Venue(venuename=form.venue.data,locationaddress=form.location.data)
        u=User(email=form.email.data,username=form.name.data,phonenumber=form.phonenumber.data)
        multi=[v,u]
        db.session.bulk_save_objects(multi)
        db.session.commit()
        e=Event(title=form.title.data,description=form.description.data,organizer_id=form.u.id,venue_id=v.id,eventtype_id=t.id,end_time="2019-05-05 22:22:22", start_time="2019-04-04 22:22:22")
        db.session.add(e)
        db.session.commit()
        flash("ok")
    return render_template('add_event.html',form=form)  

@events_blueprint.route('/list')
def list():
    return "Here all Events"