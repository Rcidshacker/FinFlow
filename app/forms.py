"""
WTForms Form Definitions
Stock & F&O Recommendation System
"""
from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, IntegerField, FloatField,
    SelectField, SelectMultipleField, RadioField, BooleanField, SubmitField
)
from wtforms.validators import (
    DataRequired, Email, Length, NumberRange, EqualTo, Optional, ValidationError
)
from app import mongo


class SignupForm(FlaskForm):
    """User registration form"""
    email = StringField('Email Address', validators=[
        DataRequired(message='Email is required'),
        Email(message='Please enter a valid email address'),
        Length(max=120)
    ])
    password = PasswordField('Password', validators=[
        DataRequired(message='Password is required'),
        Length(min=8, message='Password must be at least 8 characters')
    ])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(message='Please confirm your password'),
        EqualTo('password', message='Passwords must match')
    ])
    submit = SubmitField('Sign Up')
    
    def validate_email(self, field):
        """Check if email already exists"""
        if mongo.db.users.find_one({'email': field.data.lower()}):
            raise ValidationError('Email already registered. Please sign in.')


class SigninForm(FlaskForm):
    """User login form"""
    email = StringField('Email Address', validators=[
        DataRequired(message='Email is required'),
        Email(message='Please enter a valid email address')
    ])
    password = PasswordField('Password', validators=[
        DataRequired(message='Password is required')
    ])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')


class OnboardingStep1Form(FlaskForm):
    """Personal Information Form"""
    name = StringField('Full Name', validators=[
        DataRequired(message='Name is required'),
        Length(min=2, max=100, message='Name must be between 2 and 100 characters')
    ])
    age = IntegerField('Age', validators=[
        DataRequired(message='Age is required'),
        NumberRange(min=18, max=100, message='Age must be between 18 and 100')
    ])
    dependents = IntegerField('Number of Dependents', validators=[
        Optional(),
        NumberRange(min=0, max=20, message='Dependents must be between 0 and 20')
    ], default=0)
    submit = SubmitField('Continue')


class OnboardingStep2Form(FlaskForm):
    """Financial Information Form"""
    investment_amount = FloatField('Investment Amount (₹)', validators=[
        DataRequired(message='Investment amount is required'),
        NumberRange(min=1000, message='Minimum investment is ₹1,000')
    ])
    annual_income = SelectField('Annual Income', choices=[
        ('', 'Select your income range'),
        ('0-5L', '₹0 - ₹5 Lakhs'),
        ('5-10L', '₹5L - ₹10 Lakhs'),
        ('10-25L', '₹10L - ₹25 Lakhs'),
        ('25-50L', '₹25L - ₹50 Lakhs'),
        ('50L-1Cr', '₹50L - ₹1 Crore'),
        ('1Cr+', '₹1 Crore+')
    ], validators=[DataRequired(message='Please select your income range')])
    expected_return = FloatField('Expected Return (%)', validators=[
        DataRequired(message='Expected return is required'),
        NumberRange(min=0, max=100, message='Return must be between 0% and 100%')
    ])
    total_debt = FloatField('Total Debt (₹)', validators=[
        Optional(),
        NumberRange(min=0, message='Debt cannot be negative')
    ], default=0)
    submit = SubmitField('Continue')


class OnboardingStep3Form(FlaskForm):
    """Investment Preferences Form"""
    risk_preference = RadioField('Risk Preference', choices=[
        ('high', 'High Risk, High Reward'),
        ('moderate', 'Balanced Approach'),
        ('low', 'Capital Preservation')
    ], validators=[DataRequired(message='Please select your risk preference')])
    investment_goals = RadioField('Investment Goals', choices=[
        ('long_term', 'Long-term Wealth Building'),
        ('short_term', 'Short-term Gains')
    ], validators=[DataRequired(message='Please select your investment goal')])
    industry_interest = SelectMultipleField('Preferred Sectors', choices=[
        ('technology', 'Technology'),
        ('finance', 'Finance & Banking'),
        ('healthcare', 'Healthcare & Pharma'),
        ('energy', 'Energy & Utilities'),
        ('fmcg', 'FMCG & Consumer'),
        ('manufacturing', 'Manufacturing'),
        ('real_estate', 'Real Estate'),
        ('infrastructure', 'Infrastructure')
    ], validators=[DataRequired(message='Please select at least one sector')])
    submit = SubmitField('Continue')


class OnboardingStep4Form(FlaskForm):
    """Risk Assessment Questionnaire"""
    q1 = RadioField('Market Reaction', choices=[
        ('a', 'Sell immediately'),
        ('b', 'Wait and watch'),
        ('c', 'Buy more at lower prices')
    ], validators=[DataRequired(message='Please answer this question')])
    
    q2 = RadioField('Investment Objective', choices=[
        ('a', 'Preserve capital'),
        ('b', 'Steady income with growth'),
        ('c', 'Maximize long-term growth')
    ], validators=[DataRequired(message='Please answer this question')])
    
    q3 = RadioField('Investment Horizon', choices=[
        ('a', 'Less than 1 year'),
        ('b', '1-5 years'),
        ('c', 'More than 5 years')
    ], validators=[DataRequired(message='Please answer this question')])
    
    q4 = RadioField('Savings Percentage', choices=[
        ('a', 'Less than 20%'),
        ('b', '20% - 50%'),
        ('c', 'More than 50%')
    ], validators=[DataRequired(message='Please answer this question')])
    
    q5 = RadioField('Experience Level', choices=[
        ('a', 'Beginner'),
        ('b', 'Some experience (1-3 years)'),
        ('c', 'Experienced (3+ years)')
    ], validators=[DataRequired(message='Please answer this question')])
    
    submit = SubmitField('Complete Profile')


class ProfileEditForm(FlaskForm):
    """Profile editing form (for AJAX updates)"""
    # Personal
    name = StringField('Full Name', validators=[Optional(), Length(min=2, max=100)])
    age = IntegerField('Age', validators=[Optional(), NumberRange(min=18, max=100)])
    dependents = IntegerField('Dependents', validators=[Optional(), NumberRange(min=0, max=20)])
    
    # Financial
    investment_amount = FloatField('Investment Amount', validators=[Optional(), NumberRange(min=1000)])
    annual_income = SelectField('Annual Income', choices=[
        ('', 'Select'),
        ('0-5L', '₹0 - ₹5L'),
        ('5-10L', '₹5L - ₹10L'),
        ('10-25L', '₹10L - ₹25L'),
        ('25-50L', '₹25L - ₹50L'),
        ('50L-1Cr', '₹50L - ₹1Cr'),
        ('1Cr+', '₹1Cr+')
    ], validators=[Optional()])
    expected_return = FloatField('Expected Return', validators=[Optional(), NumberRange(min=0, max=100)])
    total_debt = FloatField('Total Debt', validators=[Optional(), NumberRange(min=0)])
    
    # Preferences
    risk_preference = RadioField('Risk Preference', choices=[
        ('high', 'High'),
        ('moderate', 'Moderate'),
        ('low', 'Low')
    ], validators=[Optional()])
    investment_goals = RadioField('Investment Goals', choices=[
        ('long_term', 'Long-term'),
        ('short_term', 'Short-term')
    ], validators=[Optional()])
