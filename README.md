# FinFlow 📈

> AI-powered Stock & F&O Recommendation System with personalized risk profiling

## Overview

FinFlow is a Flask-based web application that provides personalized investment recommendations based on user risk profiles. The system analyzes user financial data, risk tolerance, and investment goals to generate tailored stock and F&O (Futures & Options) recommendations.

## Features

- **User Authentication** - Secure signup/signin with password hashing
- **4-Step Onboarding** - Comprehensive risk profiling questionnaire
- **Risk Assessment** - Dynamic risk score calculation (0-100)
- **Stock Recommendations** - Personalized stock picks based on risk profile
- **F&O Recommendations** - Options strategies matching user's risk tolerance
- **Profile Management** - Edit profile and regenerate recommendations

---

## Quick Start

### Prerequisites

| Requirement | Version | Download                                                      |
| ----------- | ------- | ------------------------------------------------------------- |
| Python      | 3.10+   | [python.org](https://www.python.org/downloads/)               |
| MongoDB     | 6.0+    | [mongodb.com](https://www.mongodb.com/try/download/community) |

### Automated Setup (Windows)

```batch
setup.bat
```

This script will:

1. ✅ Check Python installation
2. ✅ Check MongoDB installation
3. ✅ Start MongoDB service
4. ✅ Create virtual environment
5. ✅ Install dependencies
6. ✅ Create `.env` configuration

### Manual Setup

```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file
echo SECRET_KEY=your-secret-key > .env
echo MONGO_URI=mongodb://localhost:27017/finflow >> .env

# 5. Start MongoDB service
net start MongoDB  # Windows
brew services start mongodb-community  # macOS

# 6. Run the application
python run.py
```

### Access the Application

Open your browser and navigate to: **<http://localhost:5000>**

---

## Project Structure

```text
FinFlow/
├── app/                    # Application package
│   ├── __init__.py         # App factory & extensions
│   ├── models.py           # MongoDB document models
│   ├── forms.py            # WTForms form definitions
│   ├── auth/               # Authentication blueprint
│   │   ├── routes.py       # Login, signup, logout
│   │   └── utils.py        # Auth helper functions
│   ├── main/               # Main blueprint
│   │   ├── routes.py       # Onboarding, profile, recommendations
│   │   └── utils.py        # Recommendation generator
│   ├── templates/          # Jinja2 HTML templates
│   │   ├── base.html       # Base layout
│   │   ├── landing.html    # Homepage
│   │   ├── profile.html    # User profile
│   │   ├── recommendations.html
│   │   ├── auth/           # Auth templates
│   │   └── onboarding/     # 4-step onboarding forms
│   └── static/             # Static assets
│       ├── css/            # Stylesheets
│       └── js/             # JavaScript files
├── config.py               # Configuration classes
├── run.py                  # Application entry point
├── requirements.txt        # Python dependencies
├── setup.bat               # Windows setup script
└── README.md               # This file
```

---

## Core Components

### 1. Application Factory (`app/__init__.py`)

Creates and configures the Flask application with extensions:

- **PyMongo** - MongoDB integration
- **Flask-Login** - User session management
- **Flask-Bcrypt** - Password hashing
- **Flask-WTF** - CSRF protection

### 2. Models (`app/models.py`)

| Model                 | Description                                       |
| --------------------- | ------------------------------------------------- |
| `User`                | User account with profile and authentication      |
| `StockRecommendation` | Stock picks with allocation details               |
| `FNORecommendation`   | Options strategies with profit/loss calculations  |

### 3. Onboarding Flow (`app/main/routes.py`)

| Step | Route               | Purpose                                      |
| ---- | ------------------- | -------------------------------------------- |
| 1    | `/onboarding/step1` | Personal info (age, occupation, dependents)  |
| 2    | `/onboarding/step2` | Financial info (income, investment amount)   |
| 3    | `/onboarding/step3` | Investment preferences (experience, horizon) |
| 4    | `/onboarding/step4` | Risk assessment questionnaire                |

### 4. Risk Calculation (`app/models.py`)

The `calculate_risk_profile()` function computes a risk score (0-100) based on:

- Age (younger = higher tolerance)
- Number of dependents
- Investment amount vs income ratio
- Risk preference selection
- Questionnaire responses

#### Risk Categories

| Score Range | Category     | Description                          |
| ----------- | ------------ | ------------------------------------ |
| 70-100      | Aggressive   | High risk tolerance, growth-focused  |
| 40-69       | Moderate     | Balanced approach                    |
| 0-39        | Conservative | Capital preservation priority        |

### 5. Recommendation Generator (`app/main/utils.py`)

Generates personalized recommendations based on the user's risk profile:

- Stock allocations with target prices
- F&O strategies matching risk tolerance
- Sector diversification

---

## Configuration

### Environment Variables

Create a `.env` file in the project root:

```bash
# Flask Configuration
SECRET_KEY=your-super-secret-key-change-in-production
FLASK_CONFIG=development

# MongoDB
MONGO_URI=mongodb://localhost:27017/finflow
```

### Configuration Classes (`config.py`)

| Config              | Use Case                             |
| ------------------- | ------------------------------------ |
| `DevelopmentConfig` | Local development with debug mode    |
| `ProductionConfig`  | Production with security settings    |
| `TestingConfig`     | Unit testing with test database      |

---

## API Endpoints

| Method   | Endpoint                   | Description                       |
| -------- | -------------------------- | --------------------------------- |
| GET      | `/`                        | Landing page                      |
| GET/POST | `/auth/signup`             | User registration                 |
| GET/POST | `/auth/signin`             | User login                        |
| GET      | `/auth/logout`             | User logout                       |
| GET/POST | `/onboarding/step1-4`      | Onboarding steps                  |
| GET      | `/profile`                 | User profile page                 |
| POST     | `/profile/edit`            | Update profile (AJAX)             |
| GET      | `/recommendations`         | View recommendations              |
| POST     | `/recommendations/refresh` | Regenerate recommendations (AJAX) |

---

## Technologies

| Category       | Technology                  |
| -------------- | --------------------------- |
| Backend        | Flask 3.0                   |
| Database       | MongoDB 6.0+                |
| Authentication | Flask-Login, Flask-Bcrypt   |
| Forms          | Flask-WTF, WTForms          |
| Frontend       | HTML5, CSS3, JavaScript     |
| Session        | Flask-Session (filesystem)  |

---

## Troubleshooting

### MongoDB Connection Failed

```text
Error: could not connect to server
```

**Solution:** Ensure MongoDB service is running:

```bash
net start MongoDB  # Windows
sudo systemctl start mongod  # Linux
brew services start mongodb-community  # macOS
```

### Module Not Found

```text
ModuleNotFoundError: No module named 'flask'
```

**Solution:** Activate virtual environment and reinstall:

```bash
venv\Scripts\activate
pip install -r requirements.txt
```

### Port Already in Use

```text
Address already in use
```

**Solution:** Change port in `run.py` or kill the process:

```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

---

## License

This project is for educational purposes.

---

## Credits

Made with ❤️ by FinFlow Team
