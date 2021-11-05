from flask import render_template,redirect,url_for, flash,request
from . import auth


@auth.route('/login')
def login():
    
    return "login"