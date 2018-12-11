from flask import Flask, render_template, url_for, flash, redirect
from flaskDemo.forms import ReservationForm, LoginForm, PortalForm, AvailabilityForm, FindResForm
from flask_login import login_required, current_user, logout_user, login_user
#from flaskDemo.models import Room, RoomCategory, Employee, Reservation, Guest, Billing
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY']='427d57afcc1a060879b9488a38fc7e14'
#app.config['SQLALCHEMY_DATABASE_URI'] = #Naiman's database
#db = SQLAlchemy(app)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Welcome to Hotel 453!')

@app.route("/reserve", methods=['GET', 'POST'])
def reserve():
    form = ReservationForm()
    if form.validate_on_submit():
        return redirect(url_for('availability'))
    return render_template('reserve.html', form=form)

@app.route("/availability", methods=['GET', 'POST'])
def availability():
    form = AvailabilityForm()
    if form.validate_on_submit():
        #return redirect(url_for('practice'))
            import mysql.connector
            from mysql.connector import Error
            """ Connect to MySQL database """
            try:
                conn = mysql.connector.connect(host='45.55.59.121',
                                               database='TomiBlake',
                                               user='TomiBlake',
                                               password='TomiBlake')
                if conn.is_connected():
                    print('Connected to MySQL database')
                    cursor=conn.cursor()
                else:
                    return('problem!')
                    #if wanting a dictionary use: cursor=conn.cursor(dictionary=True)
                room_type=form.room_type.data
                print(room_type)
                query="SELECT * FROM Room WHERE RoomType = %s"
                #cursor.execute("SELECT * FROM Room WHERE RoomType = %s")
                cursor.execute(query, (room_type,))
                #https://pynative.com/python-mysql-execute-parameterized-query-using-prepared-statement/

                rows = cursor.fetchall()
                # returnString=str(row)
                # #
                # while row is not None:
                # # #     #print(row)
                #     returnString+=str(row)
                # #     #print(row[1]) to access by column
                # #     #print(row['guestName']) to access as dictionary
                #     row=cursor.fetchone()
                return render_template('availability.two.html', rows=rows)

            except Error as e:
                print(e)
            finally:
                conn.close()
        # if __name__ == '__main__':
    return render_template('availability.html', form=form)

@app.route("/about")
def about():
    return render_template('about.html', title='About Our Amenities')

@app.route("/employee", methods=['GET', 'POST'])
def employee():
    if current_user.is_authenticated:
        return redirect(url_for('portal'))
    form=LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('portal'))
    return render_template('employee.html', form=form)

@app.route("/portal", methods=['GET', 'POST'])
#@login_required
#need to review webpage about login_manager
#https://flask-login.readthedocs.io/en/latest/
def portal():
    form=PortalForm()
    return render_template('portal.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/review_res", methods=['GET', 'POST'])
def review_res():
    form=FindResForm()
    if form.validate_on_submit():
        #return redirect(url_for('practice'))
            import mysql.connector
            from mysql.connector import Error
            """ Connect to MySQL database """
            try:
                conn = mysql.connector.connect(host='45.55.59.121',
                                               database='TomiBlake',
                                               user='TomiBlake',
                                               password='TomiBlake')
                if conn.is_connected():
                    print('Connected to MySQL database')
                    cursor=conn.cursor()
                else:
                    return('problem!')
                    #if wanting a dictionary use: cursor=conn.cursor(dictionary=True)
                lastName=form.lastName.data
                resNumber=form.resNumber.data
                input=(lastName, resNumber)
                print(lastName)
                print(resNumber)
                #query="SELECT * FROM Guest WHERE GuestLastName = %s"
                query="SELECT * FROM Guest WHERE (GuestLastName = %s AND ReservationNumber = %s)"
                cursor.execute(query, (lastName,resNumber))
                #https://pynative.com/python-mysql-execute-parameterized-query-using-prepared-statement/

                rows = cursor.fetchall()
                return render_template('find-reservation.html', rows=rows)

            except Error as e:
                print(e)
            finally:
                conn.close()
    return render_template('review_res.html', title='Review Reservation', form=form)
