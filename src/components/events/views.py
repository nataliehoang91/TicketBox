from flask import Blueprint, render_template,request
from src import db
from datetime import datetime
from flask import Flask, render_template, flash, redirect, url_for,request, flash

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
from flask_login import UserMixin, LoginManager,login_user,logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

# @events_blueprint.route('/')

# def hello():
#     form=AddEventForm()
    
#     return render_template('events.html',form=form) 

@events_blueprint.route('/add',methods=['POST','GET'])

def add():
    if not current_user.is_authenticated:
        flash("Please login")
        return redirect (url_for('account.login'))
    
    form=AddEventForm()
    datetime1 = datetime.strptime("2019-04-25 22:37",'%Y-%m-%d %H:%M' )
    form.eventtype.choices=[(t.id,t.event_type) for t in Type.query.all()]
    if request.method == 'POST':
        v=Venue(venuename=form.venue.data,locationaddress=form.location.data)
        
        
        # db.session.bulk_save_objects(multi)
        db.session.add(v)
      
        db.session.commit()

        print('*******', current_user.id)
        e=Event(title=form.title.data,description=form.description.data,organizer_id=current_user.id,venue_id=v.id,eventtype_id=form.eventtype.data,end_time=datetime1, start_time=datetime1,img_link=form.imglink.data,event_owner=form.eventowner.data)
        
        db.session.add(e)
        db.session.commit()
        flash('Successfully added')
    return render_template('add_event.html',form=form)  

@events_blueprint.route('/',methods=['POST','GET'])
def list():
    events = Event.query.all()

    return render_template('events.html', events = events, event_count=len(events))
