# this is the layer between the logic and the db
# we need to make the db first
from enum import unique
from classroom import db

class Student(db.Model):
    id = db.Column(db.Integer(), primary_key = True)
    firstName = db.Column(db.String(length = 20), nullable = False)
    middleName = db.Column(db.String(length = 20), nullable = False)
    lastName = db.Column(db.String(length = 20), nullable = False)
    roll = db.Column(db.String(length = 20), nullable = False, unique = True)

    def __repr__(self):
        print(
            "{} {} {}: {}".format(
                self.firstName,
                self.middleName,
                self.lastName,
                self.roll
            )
        )