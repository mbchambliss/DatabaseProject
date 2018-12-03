from flask import Flask, render_template, url_for, flash, redirect
from flaskDemo.forms import ReservationForm, LoginForm, EmployeePortalForm

app = Flask(__name__)
app.config['SECRET_KEY']='427d57afcc1a060879b9488a38fc7e14'


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Welcome to Hotel 453!')

@app.route("/reserve", methods=['GET', 'POST'])
def reserve():
    form = ReservationForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
        # This should return the availability page that shows what rooms are available
    return render_template('reserve.html', form=form)

@app.route("/about")
def about():
    return render_template('about.html', title='About Our Amenities')

@app.route("/employee", methods=['GET', 'POST'])
def employee():
    form=LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('portal'))
    return render_template('employee.html', form=form)
    # Need to ask Naiman why this doesn't work on validate

@app.route("/review_res")
def review_res():
    return render_template('review_res.html', title='Review Reservation')

@app.route("/portal", methods=['GET', 'POST'])
def portal():
    form=EmployeePortalForm()
    return render_template('portal.html', form=form)
