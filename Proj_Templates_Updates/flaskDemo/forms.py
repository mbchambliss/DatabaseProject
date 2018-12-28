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
    room_type = SelectField('Type of Room', choices=[('King Room 1', 'King Room 1'), ('King Room 2', 'King Room 2'), ('King Room 3', 'King Room 3'), ('2 Queen Beds 1', '2 Queen Beds 1'), ('2 Queen Beds 2', '2 Queen Beds 2'), ('2 Queen Beds 3', '2 Queen Beds 3'), ('Suite 1', 'Suite 1'), ('Suite 2', 'Suite 2'), ('Suite3', 'Suite3')],
                            validators=[DataRequired()])
    totalGuest = IntegerField(u'Total Number of Guests',
                        validators=[NumberRange()])
    payment = IntegerField(u'Credit Card Number',
                        validators=[NumberRange(min=10, max=16, message=None)])
    submit = SubmitField('See Availability!')

class NewHireForm(FlaskForm):
    employeeId = IntegerField(u'Employee ID',
                        validators=[NumberRange(min=1000000, max=9999999, message=None)])
    lastName = StringField('Last Name', validators=[DataRequired()])
    firstName = StringField('First Name', validators=[DataRequired()])
    phone = IntegerField(u'Phone Number',
                        validators=[NumberRange(min=1000000000, max=9999999999, message=None)])
    jobTitle = StringField('Job Title', validators=[DataRequired()])
    payGrade = IntegerField(u'Pay Grade',
                        validators=[NumberRange(min=1, max=9, message=None)])
    submit = SubmitField('Enter New Employee')

class FindResForm(FlaskForm):
    lastName = StringField('Last Name', validators=[DataRequired()])
    resNumber = IntegerField('Reservation Number', validators=[DataRequired()])
    submit = SubmitField('Find Reservation')

class UpdateResForm(FlaskForm):
     lastName = StringField('Last Name', validators=[DataRequired()])
     firstName = StringField('First Name', validators=[DataRequired()])
     resNumber = IntegerField('Reservation Number', validators=[DataRequired()])
     submit = SubmitField('Update Reservation')

class CancelResForm(FlaskForm):
    lastName = StringField('Last Name', validators=[DataRequired()])
    resNumber = IntegerField('Reservation Number', validators=[DataRequired()])
    submit = SubmitField('Cancel Reservation')

class GuestToDateForm(FlaskForm):
    arrival = DateField('Select Arrival Date', validators=[DataRequired()])
    submit = SubmitField('Submit')

class AvailabilityForm(FlaskForm):
    room_type = SelectField('Type of Room', choices=[('King Room 1', 'King Room 1'), ('King Room 2', 'King Room 2'), ('King Room 3', 'King Room 3'), ('2 Queen Beds 1', '2 Queen Beds 1'), ('2 Queen Beds 2', '2 Queen Beds 2'), ('2 Queen Beds 3', '2 Queen Beds 3'), ('Suite 1', 'Suite 1'), ('Suite 2', 'Suite 2'), ('Suite 3', 'Suite 3')],
                        validators=[DataRequired()])
    submit = SubmitField('Checkout')

class LoginForm(FlaskForm):
    employeeID = SelectField(u'EmployeeID', choices=[('4531357', '4531357'), ('4532468', '4532468',), ('4533571', '4533571'), ('4534682', '4534682'), ('4535713', '4535713'), ('4536824', '4536824'), ('4537135', '4537135'), ('4538246', '4538246',)],
                        validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class PortalForm(FlaskForm):
    arrival = DateField('Date Arriving', validators=[DataRequired()])
    submit = SubmitField('Submit')
