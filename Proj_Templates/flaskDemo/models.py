#from datetime import datetime
from flaskDemo import db

db.Model.metadata.reflect(db.engine)

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
    __table__=db.Model.metadata.tables['Billing']
