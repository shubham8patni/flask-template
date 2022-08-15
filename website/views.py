from flask import Blueprint, render_template, request

views = Blueprint('views', __name__) # not necessary to name variable same as file name and not necessay to name

@views.route('/')
def home():
    return "<h1>Hello there!!</h1>"