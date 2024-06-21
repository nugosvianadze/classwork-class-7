import os
from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from flask_login import login_user, logout_user, login_required, current_user

from .forms import RegistrationForm, LoginForm
from .models import User
from app.extensions import db, login_manager

template_folder = os.path.abspath('app/templates')
user_bp = Blueprint('user', __name__, url_prefix='/user', template_folder=template_folder)


@login_manager.user_loader
def load_user(user):
    return db.session.get(User, user)


@user_bp.route('/')
def home():
    user_id = session.get('user_id')
    user = db.session.get(User, user_id)
    return render_template('user/user-profile.html', user=user)


@user_bp.route('/login', methods=['get', 'post'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            user = User.query.filter_by(email=email, password=password).first()
            print(user)
            if not user:
                flash('Invalid Credentials, Try Again')
                return render_template('user/login.html', form=form)
            session['user_id'] = user.id
            session['username'] = user.username
            return redirect(url_for('user.home'))
        print(form.errors)
        return render_template('user/login.html', form=form)
    return render_template('user/login.html', form=form)


@user_bp.route('/register', methods=['get', 'post'])
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            email = form.email.data
            password = form.password.data
            user = User.query.filter_by(email=email).first()
            if user:
                flash('User With this Email Already Used')
                return render_template('user/registration.html', form=form)
            new_user = User(username=username, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('user.login'))
    return render_template('user/registration.html', form=form)


@user_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    flash('Successfully Logged Out!')
    return redirect(url_for('user.login'))
