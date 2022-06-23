
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify 
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
import os


app = Flask(__name__)  


@app.route('/') 
def index(): 
    return render_template('index.html')

@app.route('/ejemplo/<nombre>/<int:edad>/<ciudad>')
def ejemplo(nombre, edad, ciudad): 
    data = {
        'titulo' : 'Ejemplo', 
        'nombre' : nombre,
        'edad' : edad, 
        'ciudad' : ciudad

    }

    return render_template('ejemplo.html', data=data)


def pagina_no_encontrada(error): 
    return render_template('404.html'), 404
    #return redirect(url_for('index'))



if __name__ == '__main__': 
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True)



