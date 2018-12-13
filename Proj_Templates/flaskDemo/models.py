#from datetime import datetime
from flaskDemo import db

db.Model.metadata.reflect(db.engine)

class Room(db.Model):
    __tablename__='Room'
    __table__=db.Model.metadata.tables['Room']

class RoomCategory(db.Model):
    __tablename__='RoomCategory'
    __table__=db.Model.metadata.tables['RoomCategory']

class Employee(db.Model):
    __tablename__='Employee'
    __table__=db.Model.metadata.tables['Employee']

class Reservation(db.Model):
    __tablename__='Reservation'
    __table__=db.Model.metadata.tables['Reservation']

class Guest(db.Model):
    __tablename__='Guest'
    __table__=db.Model.metadata.tables['Guest']

class Billing(db.Model):
    __tablename__='Billing'
    __table__=db.Model.metadata.tables['Billing']
