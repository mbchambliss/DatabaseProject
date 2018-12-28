from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flaskDemo import app, db
from flaskDemo.forms import ReservationForm, LoginForm, PortalForm, AvailabilityForm, FindResForm, CancelResForm, GuestToDateForm, NewHireForm, UpdateResForm
from flask_login import login_required, current_user, logout_user, login_user
from flaskDemo.models import Billing, Employee, Guest, Reservation, Room, RoomCategory



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Welcome to Hotel 453!')

@app.route("/join")
def join():

    results = Guest.query.join(Reservation,Guest.GuestNumber == Reservation.GuestNumber) \
              .add_columns(Guest.GuestNumber, Guest.GuestFirstName, Guest.GuestLastName, Reservation.ReservationNumber, Reservation.RoomNumber)
    results2 = Guest.query.join(Reservation,Guest.GuestNumber == Reservation.GuestNumber) \
               .add_columns(Guest.GuestNumber, Guest.GuestFirstName, Guest.GuestLastName, Reservation.ReservationNumber, Reservation.RoomNumber) \
               .join(Room, Room.RoomNumber == Reservation.RoomNumber).add_columns(Room.RoomPrice)
    return render_template('join.html', title='Join',joined_1_n=results, joined_m_n=results2)

@app.route("/reserve", methods=['GET', 'POST'])
def reserve():
    form = ReservationForm()
    if form.validate_on_submit():
        return render_template('reservationConfirmation.html')
    return render_template('reserve.html', form=form)

@app.route("/newHire", methods=['GET', 'POST'])
def newHire():
    form = NewHireForm()
    if form.validate_on_submit():
        newEmp=Employee(EmployeeID=form.employeeId.data, EmployeeLastName=form.lastName.data, EmployeeFirstName=form.firstName.data, \
                        EmployeePhone=form.phone.data, EmployeeJobTitle=form.jobTitle.data, EmployeePayGrade=form.payGrade.data)
        db.session.add(newEmp)
        db.session.commit()
        print('Employee Added')
        return redirect(url_for('home'))
    return render_template('newHire.html', form=form)

@app.route("/updateRes", methods=['GET', 'POST'])
def updateRes():
    form = UpdateResForm()
    if form.validate_on_submit():
        post=Guest.query.filter_by(ReservationNumber=form.resNumber.data)
        print(post)
        post.lastName=form.lastName.data
        post.firstName=form.firstName.data
        db.session.commit(post)
        return redirect(url_for('home'))
    return render_template('updateRes.html', form=form)

@app.route("/availability", methods=['GET', 'POST'])
def availability():
    form = AvailabilityForm()
    if form.validate_on_submit():
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

                room_type=form.room_type.data
                print(room_type)
                query="SELECT * FROM Room WHERE RoomType = %s"
                cursor.execute(query, (room_type,))
                #https://pynative.com/python-mysql-execute-parameterized-query-using-prepared-statement/

                rows = cursor.fetchall()
                return render_template('availability.two.html', rows=rows)

            except Error as e:
                print(e)
            finally:
                conn.close()

    return render_template('availability.html', form=form)

@app.route("/about")
def about():
    return render_template('about.html', title='About Our Amenities')

@app.route("/employee", methods=['GET', 'POST'])
def employee():
    form=LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('portal'))
    return render_template('employee.html', form=form)

@app.route("/cancelRes", methods=['GET', 'POST'])
def cancelRes():
    form=CancelResForm()
    if form.validate_on_submit():
        print('Submit clicked')
        Reservation.query.filter_by(ReservationNumber=form.resNumber.data).delete()
        db.session.commit()
        print('Record Deleted')
        return redirect(url_for('home'))
    return render_template('cancelRes.html', form=form)

@app.route("/guestToDate", methods=['GET', 'POST'])
def guestToDate():
    form=GuestToDateForm()
    if form.validate_on_submit():
        print('Submit clicked')
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

            arrival=form.arrival.data
            print(arrival)

            query="SELECT GuestFirstName, GuestLastName FROM Guest WHERE ReservationNumber IN (SELECT ReservationNumber FROM Reservation WHERE ArrivalDate < %s)"
            cursor.execute(query, (arrival,))
            rows = cursor.fetchall()

            return render_template('find-reservation3.html', rows=rows)


        except Error as e:
            print(e)

        finally:
            conn.close()
    return render_template('guestToDate.html', form=form)

@app.route("/portal", methods=['GET', 'POST'])
def portal():
    form=PortalForm()
    print('Form loads')
    if form.validate_on_submit():
        print('Submit clicked')
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

            arrival=form.arrival.data
            print(arrival)

            query="SELECT Reservation.ReservationNumber, Guest.GuestFirstName, Guest.GuestLastName FROM Guest INNER JOIN Reservation ON Guest.ReservationNumber=Reservation.ReservationNumber WHERE ArrivalDate = %s"
            cursor.execute(query, (arrival,))
            rows = cursor.fetchall()

            count="SELECT COUNT(*) FROM Reservation WHERE ArrivalDate = %s"
            countQuery=cursor.execute(count, (arrival,))
            countQuery=cursor.fetchall()

            return render_template('find-reservation4.html', rows=rows, countQuery=countQuery)
        except Error as e:
            print(e)

        finally:
            conn.close()
    return render_template('portal.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/review_res", methods=['GET', 'POST'])
def review_res():
    form=FindResForm()
    if form.validate_on_submit():
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
                lastName=form.lastName.data
                resNumber=form.resNumber.data
                print(lastName)
                print(resNumber)
                query="SELECT * FROM Guest WHERE (GuestLastName = %s AND ReservationNumber = %s)"
                cursor.execute(query, (lastName, resNumber))
                #https://pynative.com/python-mysql-execute-parameterized-query-using-prepared-statement/

                rows = cursor.fetchall()
                return render_template('find-reservation.html', rows=rows)

            except Error as e:
                print(e)
            finally:
                conn.close()
    return render_template('review_res.html', title='Review Reservation', form=form)
