from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, IntegerField, StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, NumberRange
from wtforms.fields.html5 import DateField

class ReservationForm(FlaskForm):
    arrival = DateField('Date Arriving',
                           validators=[DataRequired()])
    departure = DateField('Date Departing',
                       validators=[DataRequired()])
    rooms = IntegerField(u'Number of Rooms',
                        validators=[NumberRange(min=1, max=7, message=None)])
    submit = SubmitField('See Availability!')

class LoginForm(FlaskForm):
    username = StringField('Username',
                        validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class EmployeePortalForm(FlaskForm):
    arrival = DateField('Date Arriving',
                        validators=[DataRequired()])
    submit = SubmitField('Submit')
    totalGuests = DateField('Total Guests',
                        validators=[DataRequired()])
