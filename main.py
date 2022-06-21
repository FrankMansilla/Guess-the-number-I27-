from flask import Flask, render_template, request, redirect, url_for, flash, jsonify 
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
import os

dbdir="sqlite///" + os.path.abspath(os.getcwd()) + "/database.db"
app = Flask(__name__) # create the application instance  
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir 
db = SQLAlchemy(app)


class Posts(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    title = db.Column(db.String(50))

@app.route('/') # at the end point /
def index(): 
    return render_template('index.html') # return the index.html template



if __name__ == '__main__':
    db.create_all()
    app.run(debug=True) # run the application



