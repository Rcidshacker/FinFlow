# Comprehensive Project Brief: Stock & F&O Recommendation System

## Project Overview
Build a modern, minimalist Flask-based web application for stock and F&O (Futures & Options) recommendations. The application features a sophisticated dark gradient theme inspired by the reference design, with smooth animations and a professional user experience.

---

## 1. Technical Stack & Architecture

### Core Technologies
- **Backend Framework:** Flask 3.0+ (Python 3.11+)
- **Frontend:** HTML5, CSS3 (with CSS Grid/Flexbox), Vanilla JavaScript (ES6+)
- **Database:** SQLite (development) / PostgreSQL (production-ready structure)
- **Authentication:** Flask-Login with secure password hashing (bcrypt)
- **Form Handling:** Flask-WTF with CSRF protection
- **Session Management:** Flask-Session with secure cookie configuration

### Project Structure
```
stock_recommendation_system/
├── app/
│   ├── __init__.py                 # Flask app factory
│   ├── models.py                   # SQLAlchemy models
│   ├── forms.py                    # WTForms definitions
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── routes.py              # Authentication routes
│   │   └── utils.py               # Auth helper functions
│   ├── main/
│   │   ├── __init__.py
│   │   ├── routes.py              # Main application routes
│   │   └── utils.py               # Business logic helpers
│   ├── static/
│   │   ├── css/
│   │   │   ├── base.css           # Global styles & variables
│   │   │   ├── auth.css           # Authentication pages
│   │   │   ├── onboarding.css     # Onboarding flow
│   │   │   ├── profile.css        # Profile page
│   │   │   └── recommendations.css # Recommendation dashboard
│   │   ├── js/
│   │   │   ├── animations.js      # Reusable animation utilities
│   │   │   ├── onboarding.js      # Onboarding form logic
│   │   │   ├── profile.js         # Profile edit functionality
│   │   │   └── recommendations.js # Charts & tab switching
│   │   └── images/
│   │       └── logo.svg           # Application logo
│   └── templates/
│       ├── base.html              # Master template
│       ├── landing.html           # Landing page
│       ├── auth/
│       │   ├── signin.html
│       │   └── signup.html
│       ├── onboarding/
│       │   ├── step1_personal.html
│       │   ├── step2_financial.html
│       │   ├── step3_preferences.html
│       │   ├── step4_questionnaire.html
│       │   └── analysis.html      # 5-second analysis screen
│       ├── profile.html
│       └── recommendations.html
├── migrations/                     # Database migrations
├── config.py                       # Configuration management
├── requirements.txt
└── run.py                         # Application entry point
```

---

## 2. Design System Specification

### Color Palette (Extracted from Reference)
```css
:root {
  /* Primary Dark Gradients */
  --gradient-primary: linear-gradient(135deg, #1F1F1F 0%, #0A1A2F 100%);
  --gradient-card: linear-gradient(160deg, #1F1F1F 0%, #0A1A2F 50%, #1F1F1F 100%);
  
  /* Accent Colors */
  --color-primary: #1F1F1F;        /* Deep charcoal */
  --color-secondary: #0A1A2F;      /* Navy blue dark */
  --color-accent: #3A86FF;         /* Bright blue accent */
  --color-highlight: #8B5CF6;      /* Purple highlight */
  
  /* Text Colors */
  --text-primary: #FFFFFF;
  --text-secondary: #B8B8B8;
  --text-muted: #6B7280;
  
  /* UI Elements */
  --border-color: rgba(255, 255, 255, 0.1);
  --card-bg: rgba(31, 31, 31, 0.8);
  --input-bg: rgba(255, 255, 255, 0.05);
  --hover-overlay: rgba(58, 134, 255, 0.1);
  
  /* Shadows & Depth */
  --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.3);
  --shadow-md: 0 4px 16px rgba(0, 0, 0, 0.4);
  --shadow-lg: 0 8px 32px rgba(0, 0, 0, 0.5);
  --shadow-glow: 0 0 20px rgba(58, 134, 255, 0.3);
}
```

### Typography System
```css
/* Font Stack */
--font-primary: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
--font-mono: 'Fira Code', 'Consolas', monospace;

/* Type Scale */
--text-xs: 0.75rem;      /* 12px */
--text-sm: 0.875rem;     /* 14px */
--text-base: 1rem;       /* 16px */
--text-lg: 1.125rem;     /* 18px */
--text-xl: 1.25rem;      /* 20px */
--text-2xl: 1.5rem;      /* 24px */
--text-3xl: 1.875rem;    /* 30px */
--text-4xl: 2.25rem;     /* 36px */
--text-5xl: 3rem;        /* 48px */

/* Font Weights */
--font-light: 300;
--font-normal: 400;
--font-medium: 500;
--font-semibold: 600;
--font-bold: 700;
```

### Spacing & Layout
```css
--spacing-xs: 0.25rem;   /* 4px */
--spacing-sm: 0.5rem;    /* 8px */
--spacing-md: 1rem;      /* 16px */
--spacing-lg: 1.5rem;    /* 24px */
--spacing-xl: 2rem;      /* 32px */
--spacing-2xl: 3rem;     /* 48px */
--spacing-3xl: 4rem;     /* 64px */

--border-radius-sm: 0.375rem;  /* 6px */
--border-radius-md: 0.5rem;    /* 8px */
--border-radius-lg: 0.75rem;   /* 12px */
--border-radius-xl: 1rem;      /* 16px */
```

### Animation System
```css
/* Transitions */
--transition-fast: 150ms cubic-bezier(0.4, 0, 0.2, 1);
--transition-base: 250ms cubic-bezier(0.4, 0, 0.2, 1);
--transition-slow: 400ms cubic-bezier(0.4, 0, 0.2, 1);

/* Easing Functions */
--ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
--ease-out: cubic-bezier(0, 0, 0.2, 1);
--ease-in: cubic-bezier(0.4, 0, 1, 1);
--ease-bounce: cubic-bezier(0.68, -0.55, 0.265, 1.55);
```

---

## 3. Page-by-Page Specifications

### 3.1 Landing Page (`landing.html`)

**Layout Requirements:**
- Full-viewport hero section with animated gradient background
- Centered content with glassmorphism card effect
- Prominent CTA buttons with hover animations
- Feature showcase section with icon-text pairs
- Smooth scroll behavior to sections

**Key Elements:**
```html
<!-- Hero Section -->
<section class="hero">
  <div class="hero-content">
    <h1 class="hero-title fade-in-up">Smart Investment Recommendations</h1>
    <p class="hero-subtitle fade-in-up delay-100">
      AI-powered stock and F&O analysis tailored to your risk profile
    </p>
    <div class="cta-group fade-in-up delay-200">
      <a href="/signup" class="btn btn-primary glow-on-hover">Get Started</a>
      <a href="/signin" class="btn btn-secondary">Sign In</a>
    </div>
  </div>
  <div class="hero-visual">
    <!-- Animated chart/graph SVG illustration -->
  </div>
</section>

<!-- Features Section -->
<section class="features">
  <div class="feature-grid">
    <div class="feature-card slide-in-left">
      <div class="feature-icon">📊</div>
      <h3>Data-Driven Insights</h3>
      <p>Real-time analysis of market trends</p>
    </div>
    <!-- Repeat for 3-4 features -->
  </div>
</section>
```

**CSS Animations:**
```css
@keyframes fade-in-up {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

.glow-on-hover:hover {
  box-shadow: 0 0 20px var(--color-accent), 0 0 40px var(--color-accent);
  transform: translateY(-2px);
}
```

---

### 3.2 Authentication Pages (`signin.html`, `signup.html`)

**Design Pattern:**
- Split-screen layout (50/50)
- Left: Form container with glassmorphism
- Right: Branded visual/gradient with subtle animation

**Form Structure (Sign Up):**
```html
<div class="auth-container">
  <div class="auth-form-section">
    <div class="auth-card">
      <h2 class="auth-title">Create Account</h2>
      <form method="POST" class="auth-form">
        {{ form.hidden_tag() }}
        
        <div class="form-group">
          <label for="email">Email Address</label>
          <input type="email" id="email" name="email" 
                 class="form-input" required
                 placeholder="your.email@example.com">
          <span class="input-icon">📧</span>
        </div>
        
        <div class="form-group">
          <label for="password">Password</label>
          <input type="password" id="password" name="password" 
                 class="form-input" required
                 placeholder="••••••••">
          <span class="input-icon toggle-password">👁️</span>
        </div>
        
        <div class="form-group">
          <label for="confirm_password">Confirm Password</label>
          <input type="password" id="confirm_password" 
                 name="confirm_password" class="form-input" required>
        </div>
        
        <button type="submit" class="btn btn-primary btn-full">
          Sign Up
          <span class="btn-arrow">→</span>
        </button>
      </form>
      
      <p class="auth-switch">
        Already have an account? 
        <a href="/signin" class="link-accent">Sign In</a>
      </p>
    </div>
  </div>
  
  <div class="auth-visual-section">
    <div class="gradient-orb"></div>
    <div class="auth-visual-content">
      <h3>Join thousands of smart investors</h3>
      <ul class="feature-list">
        <li>✓ Personalized recommendations</li>
        <li>✓ Real-time market analysis</li>
        <li>✓ Risk-optimized portfolios</li>
      </ul>
    </div>
  </div>
</div>
```

**Validation Feedback:**
- Real-time inline validation (JavaScript)
- Animated error messages sliding from input
- Password strength indicator with color coding
- Success state with checkmark animation

---

### 3.3 Onboarding Flow (Multi-Step Form)

**Step Navigation:**
```html
<div class="onboarding-container">
  <!-- Progress Bar -->
  <div class="progress-tracker">
    <div class="progress-step active" data-step="1">
      <span class="step-number">1</span>
      <span class="step-label">Personal</span>
    </div>
    <div class="progress-line active"></div>
    <div class="progress-step" data-step="2">
      <span class="step-number">2</span>
      <span class="step-label">Financial</span>
    </div>
    <div class="progress-line"></div>
    <div class="progress-step" data-step="3">
      <span class="step-number">3</span>
      <span class="step-label">Preferences</span>
    </div>
    <div class="progress-line"></div>
    <div class="progress-step" data-step="4">
      <span class="step-number">4</span>
      <span class="step-label">Risk Profile</span>
    </div>
  </div>
</div>
```

#### Step 1: Personal Information
```html
<form id="step1-form" class="onboarding-form">
  <h2 class="form-section-title">Personal Information</h2>
  
  <div class="form-row">
    <div class="form-group full-width">
      <label for="name">Full Name</label>
      <input type="text" id="name" name="name" required
             placeholder="John Doe" class="form-input">
    </div>
  </div>
  
  <div class="form-row">
    <div class="form-group half-width">
      <label for="age">Age</label>
      <input type="number" id="age" name="age" min="18" max="100" required
             placeholder="30" class="form-input">
    </div>
    
    <div class="form-group half-width">
      <label for="dependents">Number of Dependents</label>
      <input type="number" id="dependents" name="dependents" 
             min="0" max="10" value="0" class="form-input">
    </div>
  </div>
  
  <button type="button" class="btn btn-primary next-step">
    Continue <span class="btn-arrow">→</span>
  </button>
</form>
```

#### Step 2: Financial Information
```html
<form id="step2-form" class="onboarding-form">
  <h2 class="form-section-title">Financial Overview</h2>
  
  <div class="form-row">
    <div class="form-group half-width">
      <label for="investment_amount">Investment Amount (₹)</label>
      <input type="number" id="investment_amount" name="investment_amount" 
             min="0" step="1000" required placeholder="100000" 
             class="form-input currency-input">
      <span class="input-suffix">INR</span>
    </div>
    
    <div class="form-group half-width">
      <label for="annual_income">Annual Net Income</label>
      <select id="annual_income" name="annual_income" 
              required class="form-select">
        <option value="">Select Range</option>
        <option value="0-5L">₹0 - ₹5 Lakhs</option>
        <option value="5-10L">₹5L - ₹10L</option>
        <option value="10-25L">₹10L - ₹25L</option>
        <option value="25-50L">₹25L - ₹50L</option>
        <option value="50L-1Cr">₹50L - ₹1 Crore</option>
        <option value="1Cr+">₹1 Crore+</option>
      </select>
    </div>
  </div>
  
  <div class="form-row">
    <div class="form-group half-width">
      <label for="expected_return">Expected Return (%)</label>
      <input type="number" id="expected_return" name="expected_return" 
             min="0" max="100" step="0.5" required 
             placeholder="12" class="form-input">
      <div class="range-slider">
        <input type="range" min="0" max="50" step="0.5" value="12">
      </div>
    </div>
    
    <div class="form-group half-width">
      <label for="total_debt">Total Debt (₹)</label>
      <input type="number" id="total_debt" name="total_debt" 
             min="0" step="1000" value="0" 
             placeholder="0" class="form-input currency-input">
    </div>
  </div>
  
  <div class="btn-group">
    <button type="button" class="btn btn-secondary prev-step">
      ← Back
    </button>
    <button type="button" class="btn btn-primary next-step">
      Continue →
    </button>
  </div>
</form>
```

#### Step 3: Investment Preferences
```html
<form id="step3-form" class="onboarding-form">
  <h2 class="form-section-title">Investment Preferences</h2>
  
  <div class="form-group">
    <label>Risk Preference</label>
    <div class="radio-card-group">
      <label class="radio-card">
        <input type="radio" name="risk_preference" value="high" required>
        <div class="radio-card-content">
          <span class="radio-icon">🔥</span>
          <span class="radio-label">High Risk</span>
          <span class="radio-desc">Aggressive growth strategy</span>
        </div>
      </label>
      
      <label class="radio-card">
        <input type="radio" name="risk_preference" value="moderate">
        <div class="radio-card-content">
          <span class="radio-icon">⚖️</span>
          <span class="radio-label">Moderate</span>
          <span class="radio-desc">Balanced approach</span>
        </div>
      </label>
      
      <label class="radio-card">
        <input type="radio" name="risk_preference" value="low">
        <div class="radio-card-content">
          <span class="radio-icon">🛡️</span>
          <span class="radio-label">Low Risk</span>
          <span class="radio-desc">Capital preservation focus</span>
        </div>
      </label>
    </div>
  </div>
  
  <div class="form-group">
    <label>Investment Goals</label>
    <div class="radio-card-group horizontal">
      <label class="radio-card">
        <input type="radio" name="investment_goals" value="long_term" required>
        <div class="radio-card-content">
          <span class="radio-icon">📈</span>
          <span class="radio-label">Long-term (5+ years)</span>
        </div>
      </label>
      
      <label class="radio-card">
        <input type="radio" name="investment_goals" value="short_term">
        <div class="radio-card-content">
          <span class="radio-icon">⚡</span>
          <span class="radio-label">Short-term (&lt;5 years)</span>
        </div>
      </label>
    </div>
  </div>
  
  <div class="form-group">
    <label for="industry_interest">Industry of Interest</label>
    <div class="multi-select-dropdown">
      <select id="industry_interest" name="industry_interest[]" 
              multiple required class="form-select-multi">
        <option value="technology">Technology</option>
        <option value="healthcare">Healthcare</option>
        <option value="energy">Energy</option>
        <option value="finance">Finance</option>
        <option value="consumer">Consumer Goods</option>
        <option value="real_estate">Real Estate</option>
        <option value="manufacturing">Manufacturing</option>
        <option value="telecom">Telecommunications</option>
      </select>
    </div>
  </div>
  
  <div class="btn-group">
    <button type="button" class="btn btn-secondary prev-step">← Back</button>
    <button type="button" class="btn btn-primary next-step">Continue →</button>
  </div>
</form>
```

#### Step 4: Risk Profile Questionnaire
```html
<form id="step4-form" class="onboarding-form questionnaire">
  <div class="questionnaire-header">
    <h2 class="form-section-title">Risk Assessment</h2>
    <p class="form-subtitle">Answer honestly for accurate profiling</p>
  </div>
  
  <!-- Question 1 -->
  <div class="question-block">
    <h3 class="question-title">
      <span class="question-number">Q1</span>
      What is your current age group?
    </h3>
    <div class="answer-options">
      <label class="answer-option">
        <input type="radio" name="q1_age_group" value="18-30" required>
        <div class="option-content">
          <span class="option-text">18-30 years</span>
          <span class="option-badge">Higher risk capacity</span>
        </div>
      </label>
      <label class="answer-option">
        <input type="radio" name="q1_age_group" value="31-45">
        <div class="option-content">
          <span class="option-text">31-45 years</span>
          <span class="option-badge">Moderate risk capacity</span>
        </div>
      </label>
      <label class="answer-option">
        <input type="radio" name="q1_age_group" value="46-60">
        <div class="option-content">
          <span class="option-text">46-60 years</span>
          <span class="option-badge">Lower risk capacity</span>
        </div>
      </label>
      <label class="answer-option">
        <input type="radio" name="q1_age_group" value="60+">
        <div class="option-content">
          <span class="option-text">60+ years</span>
          <span class="option-badge">Conservative approach</span>
        </div>
      </label>
    </div>
  </div>
  
  <!-- Question 2 -->
  <div class="question-block">
    <h3 class="question-title">
      <span class="question-number">Q2</span>
      What is your primary investment goal?
    </h3>
    <div class="answer-options">
      <label class="answer-option">
        <input type="radio" name="q2_goal" value="aggressive" required>
        <div class="option-content">
          <span class="option-text">Maximum Growth</span>
          <span class="option-badge badge-aggressive">Aggressive</span>
        </div>
      </label>
      <label class="answer-option">
        <input type="radio" name="q2_goal" value="moderate">
        <div class="option-content">
          <span class="option-text">Wealth Accumulation</span>
          <span class="option-badge badge-moderate">Moderate</span>
        </div>
      </label>
      <label class="answer-option">
        <input type="radio" name="q2_goal" value="conservative">
        <div class="option-content">
          <span class="option-text">Income Generation</span>
          <span class="option-badge badge-conservative">Conservative</span>
        </div>
      </label>
      <label class="answer-option">
        <input type="radio" name="q2_goal" value="safe">
        <div class="option-content">
          <span class="option-text">Capital Preservation</span>
          <span class="option-badge badge-safe">Safe</span>
        </div>
      </label>
    </div>
  </div>
  
  <!-- Question 3 -->
  <div class="question-block">
    <h3 class="question-title">
      <span class="question-number">Q3</span>
      If your portfolio drops 20% in a month, what would you do?
    </h3>
    <div class="answer-options">
      <label class="answer-option">
        <input type="radio" name="q3_drop_reaction" value="buy_more" required>
        <div class="option-content">
          <span class="option-text">Invest more (Buy the dip)</span>
        </div>
      </label>
      <label class="answer-option">
        <input type="radio" name="q3_drop_reaction" value="hold">
        <div class="option-content">
          <span class="option-text">Hold patiently and wait for recovery</span>
        </div>
      </label>
      <label class="answer-option">
        <input type="radio" name="q3_drop_reaction" value="monitor">
        <div class="option-content">
          <span class="option-text">Monitor closely, might reduce exposure</span>
        </div>
      </label>
      <label class="answer-option">
        <input type="radio" name="q3_drop_reaction" value="sell">
        <div class="option-content">
          <span class="option-text">Sell immediately to prevent further losses</span>
        </div>
      </label>
    </div>
  </div>
  
  <!-- Questions 4-6: Follow same pattern -->
  <!-- Q4: Income stability -->
  <!-- Q5: Investment horizon -->
  <!-- Q6: Savings percentage -->
  
  <div class="btn-group">
    <button type="button" class="btn btn-secondary prev-step">← Back</button>
    <button type="submit" class="btn btn-primary submit-onboarding">
      Complete Profile →
    </button>
  </div>
</form>
```

#### Analysis Loading Screen (`analysis.html`)
```html
<div class="analysis-container">
  <div class="analysis-content">
    <div class="spinner-container">
      <div class="spinner-outer"></div>
      <div class="spinner-inner"></div>
      <div class="spinner-core"></div>
    </div>
    
    <h2 class="analysis-title">Analyzing Your Profile</h2>
    
    <div class="analysis-steps">
      <div class="analysis-step active" data-step="1">
        <span class="step-icon">✓</span>
        <span class="step-text">Processing financial data</span>
      </div>
      <div class="analysis-step" data-step="2">
        <span class="step-icon">⟳</span>
        <span class="step-text">Calculating risk profile</span>
      </div>
      <div class="analysis-step" data-step="3">
        <span class="step-icon">○</span>
        <span class="step-text">Generating recommendations</span>
      </div>
    </div>
    
    <div class="progress-bar">
      <div class="progress-fill"></div>
    </div>
  </div>
</div>

<script>
// Auto-advance steps with 5-second total duration
let currentStep = 1;
const totalTime = 5000;
const stepDelay = totalTime / 3;

function advanceStep() {
  if (currentStep <= 3) {
    document.querySelector(`.analysis-step[data-step="${currentStep}"]`)
      .classList.add('completed');
    currentStep++;
    if (currentStep <= 3) {
      document.querySelector(`.analysis-step[data-step="${currentStep}"]`)
        .classList.add('active');
    }
  }
  
  if (currentStep > 3) {
    setTimeout(() => {
      window.location.href = '/profile';
    }, 500);
  }
}

// Progress bar animation
document.querySelector('.progress-fill').style.animation = 
  `fillProgress ${totalTime}ms linear forwards`;

// Step advancement
setTimeout(() => advanceStep(), stepDelay);
setTimeout(() => advanceStep(), stepDelay * 2);
setTimeout(() => advanceStep(), stepDelay * 3);
</script>
```

---

### 3.4 Profile Page (`profile.html`)

**Layout Structure:**
```html
<div class="profile-container">
  <div class="profile-header">
    <div class="profile-avatar">
      <span class="avatar-initials">{{ user.name[0] }}</span>
    </div>
    <div class="profile-info">
      <h1 class="profile-name">{{ user.name }}</h1>
      <p class="profile-meta">Risk Profile: 
        <span class="risk-badge risk-{{ user.risk_profile }}">
          {{ user.risk_profile|title }}
        </span>
      </p>
    </div>
    <button class="btn btn-secondary edit-profile-btn">
      <span class="btn-icon">✏️</span> Edit Profile
    </button>
  </div>
  
  <div class="profile-sections">
    <!-- Personal Information Card -->
    <div class="profile-card">
      <div class="card-header">
        <h3 class="card-title">Personal Information</h3>
        <button class="icon-btn edit-section" data-section="personal">
          <span>✏️</span>
        </button>
      </div>
      <div class="card-body">
        <div class="info-grid">
          <div class="info-item">
            <span class="info-label">Age</span>
            <span class="info-value">{{ user.age }} years</span>
          </div>
          <div class="info-item">
            <span class="info-label">Dependents</span>
            <span class="info-value">{{ user.dependents }}</span>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Financial Overview Card -->
    <div class="profile-card">
      <div class="card-header">
        <h3 class="card-title">Financial Overview</h3>
        <button class="icon-btn edit-section" data-section="financial">
          <span>✏️</span>
        </button>
      </div>
      <div class="card-body">
        <div class="info-grid">
          <div class="info-item">
            <span class="info-label">Investment Amount</span>
            <span class="info-value currency">
              ₹{{ "{:,.0f}".format(user.investment_amount) }}
            </span>
          </div>
          <div class="info-item">
            <span class="info-label">Annual Income</span>
            <span class="info-value">{{ user.annual_income }}</span>
          </div>
          <div class="info-item">
            <span class="info-label">Expected Return</span>
            <span class="info-value">{{ user.expected_return }}%</span>
          </div>
          <div class="info-item">
            <span class="info-label">Total Debt</span>
            <span class="info-value currency">
              ₹{{ "{:,.0f}".format(user.total_debt) }}
            </span>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Investment Preferences Card -->
    <div class="profile-card">
      <div class="card-header">
        <h3 class="card-title">Investment Preferences</h3>
        <button class="icon-btn edit-section" data-section="preferences">
          <span>✏️</span>
        </button>
      </div>
      <div class="card-body">
        <div class="info-grid">
          <div class="info-item full-width">
            <span class="info-label">Risk Preference</span>
            <span class="info-value">
              <span class="risk-badge risk-{{ user.risk_preference }}">
                {{ user.risk_preference|title }} Risk
              </span>
            </span>
          </div>
          <div class="info-item full-width">
            <span class="info-label">Investment Goals</span>
            <span class="info-value">{{ user.investment_goals|replace('_', '-')|title }}</span>
          </div>
          <div class="info-item full-width">
            <span class="info-label">Industry Interests</span>
            <div class="tag-list">
              {% for industry in user.industry_interest %}
              <span class="tag">{{ industry|title }}</span>
              {% endfor %}
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Risk Profile Summary -->
    <div class="profile-card highlight">
      <div class="card-header">
        <h3 class="card-title">Risk Profile Summary</h3>
      </div>
      <div class="card-body">
        <div class="risk-score-display">
          <div class="risk-score-circle">
            <svg viewBox="0 0 100 100">
              <circle cx="50" cy="50" r="45" class="risk-score-bg"/>
              <circle cx="50" cy="50" r="45" class="risk-score-fill"
                      style="stroke-dashoffset: {{ 283 - (283 * user.risk_score / 100) }}"/>
            </svg>
            <div class="risk-score-value">{{ user.risk_score }}</div>
          </div>
          <div class="risk-score-info">
            <h4>{{ user.risk_category }}</h4>
            <p>{{ user.risk_description }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
  
  <div class="profile-actions">
    <a href="/recommendations" class="btn btn-primary btn-lg">
      View Recommendations <span class="btn-arrow">→</span>
    </a>
  </div>
</div>

<!-- Edit Modal (Appears when edit button clicked) -->
<div id="editModal" class="modal">
  <div class="modal-content">
    <div class="modal-header">
      <h3 class="modal-title">Edit Profile</h3>
      <button class="modal-close">&times;</button>
    </div>
    <div class="modal-body">
      <form id="editForm" method="POST">
        {{ form.hidden_tag() }}
        <!-- Dynamic form fields based on section being edited -->
      </form>
    </div>
    <div class="modal-footer">
      <button class="btn btn-secondary cancel-edit">Cancel</button>
      <button class="btn btn-primary save-edit">Save Changes</button>
    </div>
  </div>
</div>
```

**Edit Functionality (JavaScript):**
```javascript
// profile.js
document.querySelectorAll('.edit-section').forEach(btn => {
  btn.addEventListener('click', function() {
    const section = this.dataset.section;
    openEditModal(section);
  });
});

function openEditModal(section) {
  const modal = document.getElementById('editModal');
  const form = document.getElementById('editForm');
  
  // Populate form based on section
  form.innerHTML = generateEditForm(section);
  
  // Show modal with animation
  modal.classList.add('active');
  document.body.style.overflow = 'hidden';
}

function generateEditForm(section) {
  // Return appropriate form fields based on section
  // Implementation details...
}
```

---

### 3.5 Recommendations Page (`recommendations.html`)

**Tab-Based Layout:**
```html
<div class="recommendations-container">
  <div class="recommendations-header">
    <h1 class="page-title">Investment Recommendations</h1>
    <div class="header-meta">
      <span class="last-updated">Last updated: 2 hours ago</span>
      <button class="btn btn-secondary refresh-btn">
        <span class="btn-icon">🔄</span> Refresh
      </button>
    </div>
  </div>
  
  <!-- Tab Navigation -->
  <div class="tab-navigation">
    <button class="tab-btn active" data-tab="stocks">
      <span class="tab-icon">📊</span>
      <span class="tab-label">Stock Allocation</span>
    </button>
    <button class="tab-btn" data-tab="fno">
      <span class="tab-icon">📈</span>
      <span class="tab-label">F&O Allocation</span>
    </button>
  </div>
  
  <!-- Stocks Tab Content -->
  <div id="stocks-tab" class="tab-content active">
    <div class="allocation-summary">
      <div class="summary-card">
        <span class="summary-label">Total Allocation</span>
        <span class="summary-value">₹{{ "{:,.0f}".format(stock_allocation) }}</span>
      </div>
      <div class="summary-card">
        <span class="summary-label">Number of Stocks</span>
        <span class="summary-value">{{ stock_recommendations|length }}</span>
      </div>
      <div class="summary-card">
        <span class="summary-label">Expected Return</span>
        <span class="summary-value positive">{{ expected_return }}%</span>
      </div>
    </div>
    
    <!-- Recommendations Table -->
    <div class="recommendations-table-container">
      <table class="recommendations-table">
        <thead>
          <tr>
            <th>Stock Symbol</th>
            <th>Company Name</th>
            <th>Sector</th>
            <th>Allocation</th>
            <th>Quantity</th>
            <th>Current Price</th>
            <th>Target Price</th>
            <th>Potential Return</th>
            <th>Risk Level</th>
          </tr>
        </thead>
        <tbody>
          {% for stock in stock_recommendations %}
          <tr class="table-row">
            <td class="symbol-cell">
              <span class="symbol-badge">{{ stock.symbol }}</span>
            </td>
            <td class="company-cell">{{ stock.company_name }}</td>
            <td class="sector-cell">
              <span class="sector-tag">{{ stock.sector }}</span>
            </td>
            <td class="allocation-cell">
              ₹{{ "{:,.0f}".format(stock.allocation) }}
              <span class="allocation-percent">({{ stock.allocation_percent }}%)</span>
            </td>
            <td class="quantity-cell">{{ stock.quantity }}</td>
            <td class="price-cell">₹{{ "{:,.2f}".format(stock.current_price) }}</td>
            <td class="target-cell">₹{{ "{:,.2f}".format(stock.target_price) }}</td>
            <td class="return-cell">
              <span class="return-badge positive">+{{ stock.potential_return }}%</span>
            </td>
            <td class="risk-cell">
              <span class="risk-indicator risk-{{ stock.risk_level }}">
                {{ stock.risk_level|title }}
              </span>
            </td>
          </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
    
    <!-- Portfolio Visualization Chart -->
    <div class="chart-section">
      <h3 class="chart-title">Portfolio Distribution</h3>
      <div class="chart-container">
        <canvas id="stocksPieChart"></canvas>
      </div>
      <div class="chart-legend">
        <!-- Auto-generated legend -->
      </div>
    </div>
  </div>
  
  <!-- F&O Tab Content -->
  <div id="fno-tab" class="tab-content">
    <div class="allocation-summary">
      <div class="summary-card">
        <span class="summary-label">Total Allocation</span>
        <span class="summary-value">₹{{ "{:,.0f}".format(fno_allocation) }}</span>
      </div>
      <div class="summary-card">
        <span class="summary-label">Active Positions</span>
        <span class="summary-value">{{ fno_recommendations|length }}</span>
      </div>
      <div class="summary-card">
        <span class="summary-label">Max Risk</span>
        <span class="summary-value negative">{{ max_risk }}%</span>
      </div>
    </div>
    
    <!-- F&O Recommendations Table -->
    <div class="recommendations-table-container">
      <table class="recommendations-table">
        <thead>
          <tr>
            <th>Instrument</th>
            <th>Type</th>
            <th>Strike Price</th>
            <th>Expiry Date</th>
            <th>Position</th>
            <th>Lot Size</th>
            <th>Premium</th>
            <th>Stop Loss</th>
            <th>Target</th>
            <th>Risk Level</th>
          </tr>
        </thead>
        <tbody>
          {% for fno in fno_recommendations %}
          <tr class="table-row">
            <td class="symbol-cell">
              <span class="symbol-badge">{{ fno.instrument }}</span>
            </td>
            <td class="type-cell">
              <span class="type-badge type-{{ fno.option_type|lower }}">
                {{ fno.option_type }}
              </span>
            </td>
            <td class="strike-cell">₹{{ "{:,.0f}".format(fno.strike_price) }}</td>
            <td class="expiry-cell">{{ fno.expiry_date }}</td>
            <td class="position-cell">
              <span class="position-badge position-{{ fno.position|lower }}">
                {{ fno.position }}
              </span>
            </td>
            <td class="lot-cell">{{ fno.lot_size }}</td>
            <td class="premium-cell">₹{{ "{:,.2f}".format(fno.premium) }}</td>
            <td class="sl-cell negative">₹{{ "{:,.2f}".format(fno.stop_loss) }}</td>
            <td class="target-cell positive">₹{{ "{:,.2f}".format(fno.target) }}</td>
            <td class="risk-cell">
              <span class="risk-indicator risk-{{ fno.risk_level }}">
                {{ fno.risk_level|title }}
              </span>
            </td>
          </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
    
    <!-- Risk Analysis Chart -->
    <div class="chart-section">
      <h3 class="chart-title">Risk vs Reward Analysis</h3>
      <div class="chart-container">
        <canvas id="fnoScatterChart"></canvas>
      </div>
    </div>
  </div>
</div>
```

**Chart Implementation (Chart.js):**
```javascript
// recommendations.js
// Stocks Pie Chart
const stocksCtx = document.getElementById('stocksPieChart').getContext('2d');
const stocksPieChart = new Chart(stocksCtx, {
  type: 'doughnut',
  data: {
    labels: {{ stock_labels|tojson }},
    datasets: [{
      data: {{ stock_data|tojson }},
      backgroundColor: [
        'rgba(58, 134, 255, 0.8)',
        'rgba(139, 92, 246, 0.8)',
        'rgba(16, 185, 129, 0.8)',
        'rgba(245, 158, 11, 0.8)',
        'rgba(239, 68, 68, 0.8)',
        'rgba(236, 72, 153, 0.8)',
      ],
      borderColor: 'rgba(255, 255, 255, 0.1)',
      borderWidth: 2
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        display: false
      },
      tooltip: {
        backgroundColor: 'rgba(31, 31, 31, 0.95)',
        titleColor: '#fff',
        bodyColor: '#fff',
        borderColor: 'rgba(58, 134, 255, 0.5)',
        borderWidth: 1,
        padding: 12,
        displayColors: true,
        callbacks: {
          label: function(context) {
            return context.label + ': ₹' + context.parsed.toLocaleString();
          }
        }
      }
    }
  }
});

// F&O Scatter Chart
const fnoCtx = document.getElementById('fnoScatterChart').getContext('2d');
const fnoScatterChart = new Chart(fnoCtx, {
  type: 'scatter',
  data: {
    datasets: [{
      label: 'Call Options',
      data: {{ call_data|tojson }},
      backgroundColor: 'rgba(16, 185, 129, 0.6)',
      borderColor: 'rgba(16, 185, 129, 1)',
      pointRadius: 8,
      pointHoverRadius: 12
    }, {
      label: 'Put Options',
      data: {{ put_data|tojson }},
      backgroundColor: 'rgba(239, 68, 68, 0.6)',
      borderColor: 'rgba(239, 68, 68, 1)',
      pointRadius: 8,
      pointHoverRadius: 12
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
      x: {
        title: {
          display: true,
          text: 'Risk Level',
          color: '#B8B8B8'
        },
        grid: {
          color: 'rgba(255, 255, 255, 0.05)'
        },
        ticks: {
          color: '#B8B8B8'
        }
      },
      y: {
        title: {
          display: true,
          text: 'Potential Return (%)',
          color: '#B8B8B8'
        },
        grid: {
          color: 'rgba(255, 255, 255, 0.05)'
        },
        ticks: {
          color: '#B8B8B8'
        }
      }
    },
    plugins: {
      legend: {
        labels: {
          color: '#B8B8B8'
        }
      },
      tooltip: {
        backgroundColor: 'rgba(31, 31, 31, 0.95)',
        titleColor: '#fff',
        bodyColor: '#fff',
        borderColor: 'rgba(58, 134, 255, 0.5)',
        borderWidth: 1
      }
    }
  }
});

// Tab Switching Logic
document.querySelectorAll('.tab-btn').forEach(btn => {
  btn.addEventListener('click', function() {
    const tabName = this.dataset.tab;
    
    // Update active states
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
    
    this.classList.add('active');
    document.getElementById(`${tabName}-tab`).classList.add('active');
    
    // Trigger chart resize
    if (tabName === 'stocks') {
      stocksPieChart.resize();
    } else {
      fnoScatterChart.resize();
    }
  });
});
```

---

## 4. Animation & Interaction Specifications

### Global Animations (`animations.css`)
```css
/* Page Transitions */
.page-enter {
  animation: pageEnter 0.4s ease-out;
}

@keyframes pageEnter {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Element Fade In */
.fade-in {
  animation: fadeIn 0.6s ease-out forwards;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.fade-in-up {
  animation: fadeInUp 0.6s ease-out forwards;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Slide In Animations */
.slide-in-left {
  animation: slideInLeft 0.5s ease-out forwards;
}

@keyframes slideInLeft {
  from {
    opacity: 0;
    transform: translateX(-50px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

/* Button Hover Effects */
.btn {
  position: relative;
  overflow: hidden;
  transition: all var(--transition-base);
}

.btn::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 0;
  height: 0;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.1);
  transform: translate(-50%, -50%);
  transition: width 0.6s, height 0.6s;
}

.btn:hover::before {
  width: 300px;
  height: 300px;
}

.btn:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-glow);
}

/* Form Input Focus */
.form-input {
  transition: all var(--transition-base);
}

.form-input:focus {
  border-color: var(--color-accent);
  box-shadow: 0 0 0 3px rgba(58, 134, 255, 0.1);
  transform: translateY(-1px);
}

/* Card Hover Effect */
.profile-card, .recommendations-table-container {
  transition: all var(--transition-base);
}

.profile-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
}

/* Loading Spinner */
@keyframes spin {
  to { transform: rotate(360deg); }
}

.spinner-outer {
  animation: spin 2s linear infinite;
}

.spinner-inner {
  animation: spin 1.5s linear infinite reverse;
}

/* Progress Bar Fill */
@keyframes fillProgress {
  from { width: 0%; }
  to { width: 100%; }
}

/* Modal Animations */
.modal {
  opacity: 0;
  visibility: hidden;
  transition: all var(--transition-base);
}

.modal.active {
  opacity: 1;
  visibility: visible;
}

.modal.active .modal-content {
  animation: modalSlideIn 0.3s ease-out;
}

@keyframes modalSlideIn {
  from {
    transform: translateY(-50px) scale(0.95);
    opacity: 0;
  }
  to {
    transform: translateY(0) scale(1);
    opacity: 1;
  }
}

/* Table Row Hover */
.table-row {
  transition: all var(--transition-fast);
}

.table-row:hover {
  background: var(--hover-overlay);
  transform: translateX(4px);
}

/* Tag/Badge Animations */
.tag, .badge {
  transition: all var(--transition-fast);
}

.tag:hover {
  transform: scale(1.05);
  box-shadow: var(--shadow-sm);
}
```

---

## 5. Backend Implementation Requirements

### Database Models (`models.py`)
```python
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship to profile
    profile = db.relationship('UserProfile', backref='user', uselist=False, cascade='all, delete-orphan')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class UserProfile(db.Model):
    __tablename__ = 'user_profiles'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    # Personal Information
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    dependents = db.Column(db.Integer, default=0)
    
    # Financial Information
    investment_amount = db.Column(db.Float, nullable=False)
    annual_income = db.Column(db.String(50), nullable=False)
    expected_return = db.Column(db.Float, nullable=False)
    total_debt = db.Column(db.Float, default=0)
    
    # Investment Preferences
    risk_preference = db.Column(db.String(20), nullable=False)  # high, moderate, low
    investment_goals = db.Column(db.String(50), nullable=False)  # long_term, short_term
    industry_interest = db.Column(db.JSON, nullable=False)  # Array of industries
    
    # Questionnaire Responses (stored as JSON)
    questionnaire_answers = db.Column(db.JSON, nullable=False)
    
    # Calculated Risk Profile
    risk_score = db.Column(db.Integer, nullable=False)  # 0-100
    risk_category = db.Column(db.String(50), nullable=False)  # e.g., "Aggressive Investor"
    risk_description = db.Column(db.Text)
    
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def calculate_risk_profile(self):
        """Calculate risk score based on questionnaire answers and profile data"""
        score = 0
        answers = self.questionnaire_answers
        
        # Age group scoring (Q1)
        age_scores = {'18-30': 25, '31-45': 18, '46-60': 10, '60+': 5}
        score += age_scores.get(answers.get('q1_age_group'), 0)
        
        # Investment goal scoring (Q2)
        goal_scores = {'aggressive': 25, 'moderate': 18, 'conservative': 10, 'safe': 5}
        score += goal_scores.get(answers.get('q2_goal'), 0)
        
        # Portfolio drop reaction (Q3)
        reaction_scores = {'buy_more': 20, 'hold': 15, 'monitor': 10, 'sell': 5}
        score += reaction_scores.get(answers.get('q3_drop_reaction'), 0)
        
        # Income stability (Q4)
        stability_scores = {'very_stable': 15, 'stable': 12, 'variable': 8, 'unstable': 5}
        score += stability_scores.get(answers.get('q4_income_stability'), 0)
        
        # Investment horizon (Q5)
        horizon_scores = {'very_long': 15, 'long': 12, 'medium': 8, 'short': 5}
        score += horizon_scores.get(answers.get('q5_horizon'), 0)
        
        # Savings percentage (Q6)
        savings_scores = {'<20': 10, '20-40': 15, '40-70': 18, '>70': 5}
        score += savings_scores.get(answers.get('q6_savings_pct'), 0)
        
        self.risk_score = score
        
        # Categorize risk profile
        if score >= 80:
            self.risk_category = "Aggressive Investor"
            self.risk_description = "High risk tolerance with focus on maximum growth"
        elif score >= 60:
            self.risk_category = "Moderate-Aggressive Investor"
            self.risk_description = "Balanced approach with growth orientation"
        elif score >= 40:
            self.risk_category = "Moderate Investor"
            self.risk_description = "Balanced risk-reward with stability focus"
        elif score >= 20:
            self.risk_category = "Conservative Investor"
            self.risk_description = "Low risk tolerance prioritizing capital preservation"
        else:
            self.risk_category = "Very Conservative Investor"
            self.risk_description = "Minimal risk with primary focus on safety"
        
        db.session.commit()

class StockRecommendation(db.Model):
    __tablename__ = 'stock_recommendations'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    symbol = db.Column(db.String(20), nullable=False)
    company_name = db.Column(db.String(200), nullable=False)
    sector = db.Column(db.String(100), nullable=False)
    allocation = db.Column(db.Float, nullable=False)
    allocation_percent = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    current_price = db.Column(db.Float, nullable=False)
    target_price = db.Column(db.Float, nullable=False)
    potential_return = db.Column(db.Float, nullable=False)
    risk_level = db.Column(db.String(20), nullable=False)  # low, moderate, high
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class FNORecommendation(db.Model):
    __tablename__ = 'fno_recommendations'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    instrument = db.Column(db.String(50), nullable=False)
    option_type = db.Column(db.String(10), nullable=False)  # CALL, PUT
    strike_price = db.Column(db.Float, nullable=False)
    expiry_date = db.Column(db.Date, nullable=False)
    position = db.Column(db.String(10), nullable=False)  # LONG, SHORT
    lot_size = db.Column(db.Integer, nullable=False)
    premium = db.Column(db.Float, nullable=False)
    stop_loss = db.Column(db.Float, nullable=False)
    target = db.Column(db.Float, nullable=False)
    risk_level = db.Column(db.String(20), nullable=False)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
```

### Flask Routes Structure (`routes.py`)
```python
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from app.models import db, User, UserProfile, StockRecommendation, FNORecommendation
from app.forms import SignupForm, SigninForm, OnboardingStep1Form, OnboardingStep2Form
import time

main_bp = Blueprint('main', __name__)
auth_bp = Blueprint('auth', __name__)

# Authentication Routes
@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('main.profile'))
    
    form = SignupForm()
    if form.validate_on_submit():
        user = User(email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        
        login_user(user)
        return redirect(url_for('main.onboarding_step1'))
    
    return render_template('auth/signup.html', form=form)

@auth_bp.route('/signin', methods=['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('main.profile'))
    
    form = SigninForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('main.profile'))
        else:
            flash('Invalid email or password', 'error')
    
    return render_template('auth/signin.html', form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.landing'))

# Main Application Routes
@main_bp.route('/')
def landing():
    if current_user.is_authenticated:
        return redirect(url_for('main.profile'))
    return render_template('landing.html')

@main_bp.route('/onboarding/step1', methods=['GET', 'POST'])
@login_required
def onboarding_step1():
    # Handle step 1 form submission
    # Store data in session
    return render_template('onboarding/step1_personal.html')

# ... (Similar routes for steps 2-4)

@main_bp.route('/onboarding/complete', methods=['POST'])
@login_required
def complete_onboarding():
    # Retrieve all session data
    # Create UserProfile instance
    # Calculate risk profile
    # Generate initial recommendations
    # Redirect to analysis page
    return redirect(url_for('main.analysis'))

@main_bp.route('/analysis')
@login_required
def analysis():
    """5-second analysis screen before redirecting to profile"""
    return render_template('onboarding/analysis.html')

@main_bp.route('/profile')
@login_required
def profile():
    if not current_user.profile:
        return redirect(url_for('main.onboarding_step1'))
    
    return render_template('profile.html', user=current_user)

@main_bp.route('/profile/edit', methods=['POST'])
@login_required
def edit_profile():
    """Handle AJAX profile updates"""
    data = request.get_json()
    section = data.get('section')
    
    # Update relevant fields in UserProfile
    # Recalculate risk profile if needed
    # Return success response
    
    return jsonify({'success': True, 'message': 'Profile updated successfully'})

@main_bp.route('/recommendations')
@login_required
def recommendations():
    if not current_user.profile:
        return redirect(url_for('main.onboarding_step1'))
    
    stock_recs = StockRecommendation.query.filter_by(user_id=current_user.id).all()
    fno_recs = FNORecommendation.query.filter_by(user_id=current_user.id).all()
    
    # Prepare chart data
    stock_labels = [rec.company_name for rec in stock_recs]
    stock_data = [rec.allocation for rec in stock_recs]
    
    return render_template('recommendations.html',
                         stock_recommendations=stock_recs,
                         fno_recommendations=fno_recs,
                         stock_labels=stock_labels,
                         stock_data=stock_data)
```

---

## 6. Verification & Testing Protocol

### Prerequisites Installation (PowerShell)
```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Initialize database
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### Development Server Launch
```powershell
# Set environment variables
$env:FLASK_APP = "run.py"
$env:FLASK_ENV = "development"
$env:SECRET_KEY = "your-secret-key-here"

# Run development server
flask run --host=0.0.0.0 --port=5000
```

### Testing Checklist
1. **Landing Page**
   - [ ] Hero section animations trigger on page load
   - [ ] CTA buttons have hover effects
   - [ ] Smooth scroll to features section

2. **Authentication**
   - [ ] Sign up form validation works correctly
   - [ ] Password strength indicator displays
   - [ ] Sign in remembers user (remember me checkbox)
   - [ ] Error messages display for invalid credentials

3. **Onboarding Flow**
   - [ ] Progress bar updates correctly
   - [ ] Form validation prevents advancing with empty fields
   - [ ] Data persists when navigating between steps
   - [ ] Multi-select dropdown works for industries
   - [ ] Range slider syncs with input field
   - [ ] Questionnaire allows only one selection per question
   - [ ] Analysis screen displays for exactly 5 seconds
   - [ ] Auto-redirect to profile after analysis

4. **Profile Page**
   - [ ] All user data displays correctly
   - [ ] Risk score circle animation renders
   - [ ] Edit modal opens with prepopulated data
   - [ ] Profile updates save successfully
   - [ ] Risk profile recalculates when relevant fields change

5. **Recommendations Page**
   - [ ] Tab switching works smoothly
   - [ ] Stock allocation table displays correctly
   - [ ] F&O allocation table displays correctly
   - [ ] Charts render properly (Chart.js)
   - [ ] Hover effects on table rows work
   - [ ] Data refreshes when refresh button clicked

6. **Responsive Design**
   - [ ] Test on viewport widths: 320px, 768px, 1024px, 1920px
   - [ ] All elements stack correctly on mobile
   - [ ] Touch interactions work on tablets
   - [ ] No horizontal scrolling on any device

7. **Performance**
   - [ ] Page load time < 2 seconds
   - [ ] Smooth 60fps animations
   - [ ] No layout shifts during load
   - [ ] Images optimized (WebP format where supported)

---

## 7. Final Deliverables Summary

Upon completion, the following should be production-ready:

### Code Structure
```
✓ Modular Flask application with blueprints
✓ SQLAlchemy models with relationships
✓ WTForms with validation
✓ Secure authentication with Flask-Login
✓ CSRF protection enabled
✓ Environment-based configuration
```

### Frontend Assets
```
✓ Responsive HTML5 templates (Jinja2)
✓ Modular CSS with design system
✓ Vanilla JavaScript (no framework dependencies)
✓ Chart.js integration for visualizations
✓ Optimized images and SVG icons
```

### User Experience
```
✓ Smooth page transitions
✓ Form validation feedback
✓ Loading states for async operations
✓ Error handling with user-friendly messages
✓ Accessibility (ARIA labels, keyboard navigation)
```

### Documentation
```
✓ README with setup instructions
✓ requirements.txt with pinned versions
✓ Database migration scripts
✓ Inline code comments
✓ API endpoint documentation (if applicable)
```

---

## 8. Additional Best Practices

### Security Considerations
- All forms use CSRF tokens
- Passwords hashed with bcrypt (minimum 12 cost factor)
- SQL injection prevention via SQLAlchemy ORM
- XSS prevention through template auto-escaping
- Secure session cookies (httponly, secure flags in production)
- Rate limiting on authentication endpoints

### Performance Optimization
- Lazy load images below the fold
- Minify CSS/JS in production
- Enable gzip compression
- Database query optimization (eager loading for relationships)
- Implement caching for static recommendations

### Code Quality Standards
- Follow PEP 8 style guide for Python
- Use ESLint for JavaScript
- Consistent naming conventions (snake_case for Python, camelCase for JS)
- DRY principle (Don't Repeat Yourself)
- Comprehensive error handling with try-catch blocks
- Logging for debugging (Python logging module)

---

This comprehensive brief provides everything needed to build a professional, modern stock recommendation system with Flask. The dark gradient theme, smooth animations, and user-centric design will create an engaging experience while maintaining clean code architecture and security best practices.