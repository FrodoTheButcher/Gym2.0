from flask import Flask
from flask import render_template , redirect , request , url_for , flash , abort
from PROJECT import app,db
from PROJECT.form import Register
from PROJECT.models import User

@app.route("/")
def base():
    return render_template('base.html')

@app.route("/LOGIN")
def login():
    return render_template('login.html')

@app.route("/REGISTERMUIE")
def register():
    return render_template('register.html')


if __name__=='__main__':
    app.run(debug=True)