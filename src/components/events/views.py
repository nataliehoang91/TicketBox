from flask import Blueprint, render_template,request
from src import db
from datetime import datetime
from flask import Flask, render_template, flash, redirect, url_for,request

# from flask_login import UserMixin, LoginManager,login_user,logout_user, current_user, login_required
# from flask import request
# from flask import session
# from DateTime import DateTime




events_blueprint=Blueprint('events',__name__,template_folder='../../templates/events')


from src.components.events.forms import AddEventForm
from src.models.user import User
from src.models.event import Event
from src.models.venue import Venue
from src.models.type import Type

@events_blueprint.route('/')
def hello():
    form=AddEventForm()
    
    return render_template('events.html',form=form) 

@events_blueprint.route('/add',methods=['POST','GET'])


def add():
    form=AddEventForm()
    
    datetime1 = datetime.strptime("2019-04-25 22:37",'%Y-%m-%d %H:%M' )
    form.eventtype.choices=[(t.id,t.event_type) for t in Type.query.all()]
    if request.method == 'POST':
        v=Venue(venuename=form.venue.data,locationaddress=form.location.data)
        u=User(email=form.email.data,username=form.name.data,phonenumber=form.phonenumber.data)
        multi=[v,u]
        # db.session.bulk_save_objects(multi)
        db.session.add(v)
        db.session.add(u)
        db.session.commit()

        print('*******', u.id)
        e=Event(title=form.title.data,description=form.description.data,organizer_id=u.id,venue_id=v.id,eventtype_id=form.eventtype.data,end_time=datetime1, start_time=datetime1)
        
        db.session.add(e)
        db.session.commit()
       
    return render_template('add_event.html',form=form)  

@events_blueprint.route('/list',methods=['POST','GET'])
def list():
    return render_template('events.html', events= Event.query.all())
