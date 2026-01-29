"""
Flask Application Factory
Stock & F&O Recommendation System
"""
from flask import Flask
from flask_pymongo import PyMongo
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect
from config import config

# Initialize extensions
mongo = PyMongo()
login_manager = LoginManager()
bcrypt = Bcrypt()
csrf = CSRFProtect()

# Configure login manager
login_manager.login_view = 'auth.signin'
login_manager.login_message = 'Please sign in to access this page.'
login_manager.login_message_category = 'info'


def create_app(config_name='default'):
    """Application factory function"""
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config[config_name])
    
    # Initialize extensions with app
    mongo.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    csrf.init_app(app)
    
    # User loader for Flask-Login
    from app.models import User
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.get_by_id(user_id)
    
    # Register blueprints
    from app.auth import auth_bp
    from app.main import main_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    
    # Create indexes for better performance
    with app.app_context():
        try:
            mongo.db.users.create_index('email', unique=True)
            mongo.db.stock_recommendations.create_index('user_id')
            mongo.db.fno_recommendations.create_index('user_id')
        except Exception:
            pass  # Indexes may already exist
    
    return app
