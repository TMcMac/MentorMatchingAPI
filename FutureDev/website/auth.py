from flask import Blueprint, render_template, request, flash, redirect, url4
from email_validator import validate_email, EmailNotValidError
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", text="Testing", user="Tim")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        password = request.form.get('password')
        confirmPassword = request.form.get('confirmPassword')

        if (check(email) == False):
            flash('Email is not valid.', category='error')
        elif len(firstName) < 2:
            flash('First Name must be greater than 1 characters.', category='error')
        elif len(lastName) < 2:
            flash('Last Name must be greater than 1 characters.', category='error')
        elif password != confirmPassword:
            flash('Passwords do not match', category='error')
        elif len(password) < 8:
            flash('Password must be 8 characters or greater.', category='error')
        else:
            new_user = User(email=email, firstName=firstName, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully!', category='success')


    return render_template("signup.html")



# Check email for validity before user sign up processes
def check(email):
    is_new_account = True # False for login pages

    try:
    # validate and get info
        validation = validate_email(email, check_deliverability=is_new_account)
        # replace with normalized form
        # email = v["email"]
        return True
    except EmailNotValidError as e:
        # email is not valid, exception message is human-readable
        print(str(e))
        return False