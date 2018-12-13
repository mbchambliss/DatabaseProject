#from datetime import datetime
from flaskDemo import db

"""db.Model.metadata.reflect(db.engine)

class Room(db.Model):
    __table__=db.Model.metadata.tables['Room']

class RoomCategory(db.Model):
    __table__=db.Model.metadata.tables['RoomCategory']

class Employee(db.Model):
    __table__=db.Model.metadata.tables['Employee']

class Reservation(db.Model):
    __table__=db.Model.metadata.tables['Reservation']

class Guest(db.Model):
    __table__=db.Model.metadata.tables['Guest']

class Billing(db.Model):
    __table__=db.Model.metadata.tables['Billing']"""

class Billing(db.Model):
    __tablename__='Billing'
    BillingNumber = db.Column(db.Integer, primary_key=True)
    ReservationNumber = db.Column(db.Integer, db.ForeignKey('Reservation.ReservationNumber'), nullable=False)
    GuestNumber = db.Column(db.Integer, db.ForeignKey('Guest.GuestNumber'), nullable=False)

class Employee(db.Model):
    __tablename__='Employee'
    EmployeeID = db.Column(db.Integer, primary_key=True)
    EmployeeFirstName = db.Column(db.String(20), nullable=False)
    EmployeeLastName = db.Column(db.String(20), nullable=False)
    EmployeePhone = db.Column(db.String(10), nullable=False)
    EmployeeJobTitle = db.Column(db.String(25), nullable=False)
    EmployeePayGrade = db.Column(db.Integer, nullable=True)

class Guest(db.Model):
    __tablename__='Guest'
    GuestNumber = db.Column(db.Integer, primary_key=True)
    ReservationNumber = db.Column(db.Integer, nullable=False)
    GuestFirstName = db.Column(db.String(15), nullable=False)
    GuestLastName = db.Column(db.String(20), nullable=False)
    GuestAddress = db.Column(db.String(20), nullable=False)
    GuestCity = db.Column(db.String(20), nullable=False)
    GuestState = db.Column(db.String(2), nullable=False)
    GuestCountry = db.Column(db.String(15), nullable=False)
    GuestZipCode = db.Column(db.String(10), nullable=False)
    GuestPhone = db.Column(db.String(10), nullable=False)
    GuestEmail = db.Column(db.String(30), nullable=False)
    CreditCardNumber = db.Column(db.String(19), nullable=False)

class Reservation(db.Model):
    __tablename__='Reservation'
    #id = db.Column(db.Integer, primary_key=True)
    ReservationNumber = db.Column(db.Integer, primary_key=True)
    GuestNumber = db.Column(db.Integer, db.ForeignKey('Guest.GuestNumber'), nullable=False)
    EmployeeID = db.Column(db.Integer, db.ForeignKey('Employee.EmployeeID'), nullable=False)
    RoomNumber = db.Column(db.Integer, db.ForeignKey('Room.RoomNumber'), nullable=False)
    ReservationDate = db.Column(db.Date, nullable=False)
    ArrivalDate = db.Column(db.Date, nullable=False)
    DepartureDate = db.Column(db.Date, nullable=False)
    TotalNightStay = db.Column(db.Integer, nullable=False)
    TotalGuests = db.Column(db.Integer, nullable=False)
    TotalCost = db.Column(db.Numeric, nullable=False)
    CreditCardNumber = db.Column(db.String(19), nullable=False)

class Room(db.Model):
    __tablename__='Room'
    #id = db.Column(db.Integer, primary_key=True)
    RoomNumber = db.Column(db.Integer, primary_key=True)
    RoomType = db.Column(db.String(20), db.ForeignKey('RoomCategory.RoomType'), nullable=False)
    GuestNumber = db.Column(db.Integer, nullable=False)
    ReservationNumber = db.Column(db.Integer, nullable=False)
    RoomPrice = db.Column(db.Numeric, nullable=False)

class RoomCategory(db.Model):
    __tablename__='RoomCategory'
    #id = db.Column(db.Integer, primary_key=True)
    RoomType = db.Column(db.String(20), primary_key=True)
    RoomDescription = db.Column(db.String(40), nullable=False)
    RoomCapacity = db.Column(db.Integer, nullable=False)

  
