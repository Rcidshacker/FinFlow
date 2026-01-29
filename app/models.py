"""
MongoDB Document Models
Stock & F&O Recommendation System
"""
from datetime import datetime
from bson import ObjectId
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import mongo


class User(UserMixin):
    """User model for authentication"""
    
    def __init__(self, user_data):
        self._id = user_data.get('_id')
        self.email = user_data.get('email')
        self.password_hash = user_data.get('password_hash')
        self.created_at = user_data.get('created_at', datetime.utcnow())
        self._is_active = user_data.get('is_active', True)
        self.profile = user_data.get('profile')
    
    @property
    def is_active(self):
        return self._is_active
    
    def get_id(self):
        return str(self._id)
    
    @staticmethod
    def get_by_id(user_id):
        """Get user by ID"""
        try:
            user_data = mongo.db.users.find_one({'_id': ObjectId(user_id)})
            if user_data:
                return User(user_data)
        except Exception:
            pass
        return None
    
    @staticmethod
    def get_by_email(email):
        """Get user by email"""
        user_data = mongo.db.users.find_one({'email': email.lower()})
        if user_data:
            return User(user_data)
        return None
    
    @staticmethod
    def create(email, password):
        """Create a new user"""
        user_data = {
            'email': email.lower(),
            'password_hash': generate_password_hash(password),
            'created_at': datetime.utcnow(),
            'is_active': True,
            'profile': None
        }
        result = mongo.db.users.insert_one(user_data)
        user_data['_id'] = result.inserted_id
        return User(user_data)
    
    def check_password(self, password):
        """Verify password"""
        return check_password_hash(self.password_hash, password)
    
    def update_profile(self, profile_data):
        """Update user profile"""
        # Calculate risk profile
        profile_data = calculate_risk_profile(profile_data)
        profile_data['updated_at'] = datetime.utcnow()
        
        mongo.db.users.update_one(
            {'_id': self._id},
            {'$set': {'profile': profile_data}}
        )
        self.profile = profile_data
    
    def __repr__(self):
        return f'<User {self.email}>'


def calculate_risk_profile(profile_data):
    """Calculate risk score and category based on profile data"""
    score = 50  # Base score
    
    # Age factor (younger = higher risk tolerance)
    age = profile_data.get('age', 30)
    if age < 30:
        score += 15
    elif age < 40:
        score += 10
    elif age < 50:
        score += 5
    elif age >= 60:
        score -= 10
    
    # Dependents factor (more = more conservative)
    dependents = profile_data.get('dependents', 0)
    score -= dependents * 3
    
    # Investment amount relative to income
    investment = profile_data.get('investment_amount', 0)
    income_ranges = {
        '0-5L': 250000,
        '5-10L': 750000,
        '10-25L': 1750000,
        '25-50L': 3750000,
        '50L-1Cr': 7500000,
        '1Cr+': 15000000
    }
    annual_income = income_ranges.get(profile_data.get('annual_income', '5-10L'), 750000)
    
    if investment < annual_income * 0.2:
        score += 5
    elif investment > annual_income * 0.5:
        score -= 5
    
    # Risk preference factor
    risk_pref = profile_data.get('risk_preference', 'moderate')
    if risk_pref == 'high':
        score += 20
    elif risk_pref == 'low':
        score -= 20
    
    # Questionnaire answers
    answers = profile_data.get('questionnaire_answers', {})
    for key, value in answers.items():
        if value == 'c':  # Aggressive
            score += 5
        elif value == 'a':  # Conservative
            score -= 5
    
    # Clamp score between 0 and 100
    score = max(0, min(100, score))
    
    # Determine category
    if score >= 70:
        category = 'Aggressive'
        description = 'You have a high risk tolerance and are comfortable with market volatility in pursuit of higher returns.'
    elif score >= 40:
        category = 'Moderate'
        description = 'You seek a balance between growth and stability, accepting some risk for better returns.'
    else:
        category = 'Conservative'
        description = 'You prioritize capital preservation and prefer stable, low-risk investments.'
    
    profile_data['risk_score'] = score
    profile_data['risk_category'] = category
    profile_data['risk_description'] = description
    
    return profile_data


class StockRecommendation:
    """Stock recommendation model"""
    
    def __init__(self, data):
        self._id = data.get('_id')
        self.user_id = data.get('user_id')
        self.symbol = data.get('symbol')
        self.company_name = data.get('company_name')
        self.sector = data.get('sector')
        self.current_price = data.get('current_price')
        self.target_price = data.get('target_price')
        self.allocation_amount = data.get('allocation_amount')
        self.allocation_percent = data.get('allocation_percent')
        self.expected_return = data.get('expected_return')
        self.risk_level = data.get('risk_level')
        self.rationale = data.get('rationale')
        self.created_at = data.get('created_at', datetime.utcnow())
    
    @staticmethod
    def get_by_user(user_id):
        """Get all stock recommendations for a user"""
        recs = mongo.db.stock_recommendations.find({'user_id': ObjectId(user_id)})
        return [StockRecommendation(r) for r in recs]
    
    @staticmethod
    def create(user_id, rec_data):
        """Create a new stock recommendation"""
        rec_data['user_id'] = ObjectId(user_id)
        rec_data['created_at'] = datetime.utcnow()
        result = mongo.db.stock_recommendations.insert_one(rec_data)
        rec_data['_id'] = result.inserted_id
        return StockRecommendation(rec_data)
    
    @staticmethod
    def delete_by_user(user_id):
        """Delete all recommendations for a user"""
        mongo.db.stock_recommendations.delete_many({'user_id': ObjectId(user_id)})


class FNORecommendation:
    """F&O recommendation model"""
    
    def __init__(self, data):
        self._id = data.get('_id')
        self.user_id = data.get('user_id')
        self.symbol = data.get('symbol')
        self.option_type = data.get('option_type')  # CALL or PUT
        self.position = data.get('position')  # LONG or SHORT
        self.strike_price = data.get('strike_price')
        self.expiry = data.get('expiry')
        self.premium = data.get('premium')
        self.quantity = data.get('quantity')
        self.max_profit = data.get('max_profit')
        self.max_loss = data.get('max_loss')
        self.strategy_name = data.get('strategy_name')
        self.rationale = data.get('rationale')
        self.created_at = data.get('created_at', datetime.utcnow())
    
    @staticmethod
    def get_by_user(user_id):
        """Get all F&O recommendations for a user"""
        recs = mongo.db.fno_recommendations.find({'user_id': ObjectId(user_id)})
        return [FNORecommendation(r) for r in recs]
    
    @staticmethod
    def create(user_id, rec_data):
        """Create a new F&O recommendation"""
        rec_data['user_id'] = ObjectId(user_id)
        rec_data['created_at'] = datetime.utcnow()
        result = mongo.db.fno_recommendations.insert_one(rec_data)
        rec_data['_id'] = result.inserted_id
        return FNORecommendation(rec_data)
    
    @staticmethod
    def delete_by_user(user_id):
        """Delete all F&O recommendations for a user"""
        mongo.db.fno_recommendations.delete_many({'user_id': ObjectId(user_id)})
