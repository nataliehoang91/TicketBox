from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField,SubmitField,DateTimeField,SelectField,validators

class AddEventForm(FlaskForm):
    description=StringField('Description of Event: ',[validators.Length(min=4,max=25)])
    venue=SelectField('Venue' ,coerce=int)
    organizer=SelectField('Organizer' ,coerce=int)
    submit=SubmitField('Add Event')