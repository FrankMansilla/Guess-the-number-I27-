from flask import Flask, render_template, request, redirect, url_for, flash, jsonify 
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from utils.db import db
from models import User
from models.User import User
from routes import reglas

app = Flask(__name__)  


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Frank?1234@localhost/GuessTheNumber'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
SQLAlchemy(app)

with app.app_context():
    db.create_all()


@app.route('/', methods=['POST', 'GET']) 
def index(): 
  return render_template('index.html')

@app.route('/')
def rules(): 
    return render_template('reglas.html')
 
def pagina_no_encontrada(error): 
    return render_template('404.html'), 404
    #return redirect(url_for('index'))



if __name__ == '__main__': 
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True)



