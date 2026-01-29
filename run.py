"""
Application Entry Point
Stock & F&O Recommendation System
"""
import os
from app import create_app

# Get configuration from environment
config_name = os.environ.get('FLASK_CONFIG', 'development')
app = create_app(config_name)

if __name__ == '__main__':
    # Run the development server
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
