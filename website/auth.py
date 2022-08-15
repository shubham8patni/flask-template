from unicodedata import category
from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__) # not necessary to name variable same as file name and not necessay to name


@auth.route('/login', methods = ['GET','POST'])
def login():
    flash("Hello There!!", category='success')
    return render_template("login.html")


@auth.route('/logout')
def logout():
    return "Logout"


@auth.route('/register', methods = ['GET','POST'])
def register():
    return "Register"