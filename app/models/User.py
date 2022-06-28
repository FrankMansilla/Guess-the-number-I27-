from cmath import e
from utils.db import db


class User(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    fullname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(18))


    def __init__(self, name, fullname, email, password):
        self.name = name
        self.fullname = fullname
        self.email = email
        self.password = password 


