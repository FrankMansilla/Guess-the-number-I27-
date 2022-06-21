from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__) # create the application instance 


@app.route('/') # at the end point /
def index(): 
    return render_template('index.html') # return the index.html template

if __name__ == '__main__':
    app.run(debug=True) # run the application



