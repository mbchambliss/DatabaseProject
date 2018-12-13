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
    room_type = SelectField('Type of Room', choices=[('King Room 1', 'King Room 1'), ('King Room 2', 'King Room 2'), ('King Room 1', 'King Room 3'), ('2 Queen Beds 1', '2 Queen Beds 1'), ('2 Queen Beds 2', '2 Queen Beds 2'), ('2 Queen Beds 3', '2 Queen Beds 3'), ('Suite 1', 'Suite 1'), ('Suite 2', 'Suite 2')],
                            validators=[DataRequired()])
    totalGuest = IntegerField(u'Total Number of Guests',
                        validators=[NumberRange(min=1, max=8, message=None)])
    payment = IntegerField(u'Credit Card Number',
                        validators=[NumberRange(min=10, max=16, message=None)])
    submit = SubmitField('See Availability!')

class FindResForm(FlaskForm):
    lastName = StringField('Last Name', validators=[DataRequired()])
    resNumber = IntegerField('Reservation Number', validators=[DataRequired()])
    submit = SubmitField('Find Reservation')

# class UpdateResForm(FlaskForm):
#     lastName = StringField('Last Name', validators=[DataRequired()])
#     resNumber = IntegerField('Reservation Number', validators=[DataRequired()])
#     submit = SubmitField('Find Reservation')

class CancelResForm(FlaskForm):
    lastName = StringField('Last Name', validators=[DataRequired()])
    resNumber = IntegerField('Reservation Number', validators=[DataRequired()])
    submit = SubmitField('Cancel Reservation')

class GuestToDateForm(FlaskForm):
    arrival = DateField('Select Arrival Date', validators=[DataRequired()])
    submit = SubmitField('Submit')

class AvailabilityForm(FlaskForm):
    room_type = SelectField('Type of Room', choices=[('King Room 1', 'King Room 1'), ('King Room 2', 'King Room 2'), ('King Room 1', 'King Room 3'), ('2 Queen Beds 1', '2 Queen Beds 1'), ('2 Queen Beds 2', '2 Queen Beds 2'), ('2 Queen Beds 3', '2 Queen Beds 3'), ('Suite 1', 'Suite 1'), ('Suite 2', 'Suite 2')],
                        validators=[DataRequired()])
    submit = SubmitField('Checkout')

class LoginForm(FlaskForm):
    username = StringField('Username',
                        validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class PortalForm(FlaskForm):
    arrival = DateField('Date Arriving', validators=[DataRequired()])
    submit = SubmitField('Submit')

# class PortalForm(FlaskForm):
#     arrival = DateField('Date Arriving',format='%m-%d-%Y')
#     submit = SubmitField('Submit')
