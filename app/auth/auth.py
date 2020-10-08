# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2020 -zinken7
"""

from flask import jsonify, render_template, redirect, request, url_for
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user
)

from app import db, login_manager
from app.auth import blueprint
from app.forms import LoginForm, CreateAccountForm
from app.models import User

from app.auth.util import verify_pass

## Login & Registration
@blueprint.route('/login/', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    if 'login' in request.form:
        
        # read form data
        username = request.form['username']
        password = request.form['password']

        # Locate user
        user = User.query.filter_by(username=username).first()
        
        # Check the password
        if user and verify_pass( password, user.password):

            login_user(user)
            return redirect(url_for('auth_blueprint.login'))

        # Something (user or pass) is not ok
        return render_template( 'auth/accounts/login.html', msg='Wrong user or password', form=login_form)

    if not current_user.is_authenticated:
        return render_template( 'auth/accounts/login.html', form=login_form)
    
    return redirect(url_for('admin_blueprint.index'))

@blueprint.route('/register/', methods=['GET', 'POST'])
def register():
    login_form = LoginForm(request.form)
    create_account_form = CreateAccountForm(request.form)
    if 'register' in request.form:

        username  = request.form['username']
        email     = request.form['email'   ]

        user = User.query.filter_by(username=username).first()
        if user:
            return render_template( 'auth/accounts/register.html', msg='Username already registered', success=False, form=create_account_form)

        user = User.query.filter_by(email=email).first()
        if user:
            return render_template( 'auth/accounts/register.html', msg='Email already registered', success=False, form=create_account_form)

        # else we can create the user
        user = User(**request.form)
        db.session.add(user)
        db.session.commit()

        return render_template( 'auth/accounts/register.html', msg='User created please <a href="/login">login</a>', success=True, form=create_account_form)

    else:
        return render_template( 'auth/accounts/register.html', form=create_account_form)

@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth_blueprint.login'))
