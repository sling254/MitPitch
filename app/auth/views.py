from flask import render_template,url_for,flash,redirect,request
from . import auth
from flask_login import login_user,login_required,logout_user
from .forms import RegForm,LoginForm
from ..models import User
from .. import db
from ..email import mail_message



@auth.route('/login')
def login():
    
    return render_template('auth/login.html')



@auth.route('/register', methods = ["GET","POST"])
def register():
  form = RegForm()
  if form.validate_on_submit():
    user = User(email = form.email.data, username = form.username.data, password = form.password.data)
    user.save_u()
    mail_message("Welcome to the Pitch","email/welcome_user",user.email,user=user)
    return redirect(url_for('auth.login'))
  return render_template('auth/register.html', form = form)