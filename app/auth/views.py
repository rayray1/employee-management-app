# app/auth/views.py

from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import auth
from .forms import LoginForm, RegistrationForm
from .. import db
from ..models import Employee


# register employees(add to db)
@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        employee = Employee(first_name=form.first_name.data,
                            last_name=form.last_name.data,
                            email=form.email.data,
                            password=form.password.data)

        # add employee to db
        db.session.add(employee)
        db.session.commit()
        flash('You have successfully registered.')

        # redirect form to login page
        return redirect(url_for('auth.login'))

    # load registration template
    return render_template('auth/register.html', form=form, title='Register')



# login employees
@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        employee = Employee.query.filter_by(email=form.email.data).first()
        if employee is not None and employee.verify_password(form.password.data):
            login_user(employee)
            if employee.is_admin:
                return redirect(url_for('home.admin_dashboard'))
            else:
                return redirect(url_for('home.dashboard'))
        else:
            flash('Invalid email or password.')
    return render_template('auth/login.html', form=form, title='Login')



# logout
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Goodbye!')
    return redirect(url_for('auth.login'))
