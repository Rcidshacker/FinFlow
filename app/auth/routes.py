"""
Authentication Routes
Handles signup, signin, and logout functionality
"""
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.auth import auth_bp
from app.forms import SignupForm, SigninForm
from app.models import User


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    """User registration route"""
    if current_user.is_authenticated:
        if current_user.profile:
            return redirect(url_for('main.recommendations'))
        return redirect(url_for('main.onboarding_step1'))
    
    form = SignupForm()
    
    if form.validate_on_submit():
        # Create new user
        user = User.create(
            email=form.email.data,
            password=form.password.data
        )
        
        # Log the user in
        login_user(user)
        flash('Account created successfully! Let\'s set up your profile.', 'success')
        return redirect(url_for('main.onboarding_step1'))
    
    return render_template('auth/signup.html', form=form)


@auth_bp.route('/signin', methods=['GET', 'POST'])
def signin():
    """User login route"""
    if current_user.is_authenticated:
        if current_user.profile:
            return redirect(url_for('main.recommendations'))
        return redirect(url_for('main.onboarding_step1'))
    
    form = SigninForm()
    
    if form.validate_on_submit():
        user = User.get_by_email(form.email.data)
        
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('Welcome back!', 'success')
            
            # Redirect to next page or appropriate dashboard
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            
            if user.profile:
                return redirect(url_for('main.recommendations'))
            return redirect(url_for('main.onboarding_step1'))
        else:
            flash('Invalid email or password.', 'error')
    
    return render_template('auth/signin.html', form=form)


@auth_bp.route('/logout')
@login_required
def logout():
    """User logout route"""
    logout_user()
    flash('You have been signed out.', 'info')
    return redirect(url_for('main.landing'))
