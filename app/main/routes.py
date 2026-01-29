"""
Main Application Routes
Landing, onboarding, profile, and recommendations
"""
from flask import render_template, redirect, url_for, flash, request, session, jsonify
from flask_login import login_required, current_user
from app.main import main_bp
from app.forms import (
    OnboardingStep1Form, OnboardingStep2Form,
    OnboardingStep3Form, OnboardingStep4Form
)
from app.models import StockRecommendation, FNORecommendation
from app.main.utils import generate_recommendations


@main_bp.route('/')
def landing():
    """Landing page"""
    if current_user.is_authenticated:
        if current_user.profile:
            return redirect(url_for('main.recommendations'))
        return redirect(url_for('main.onboarding_step1'))
    return render_template('landing.html')


# ==================== ONBOARDING ====================

@main_bp.route('/onboarding/step1', methods=['GET', 'POST'])
@login_required
def onboarding_step1():
    """Step 1: Personal Information"""
    if current_user.profile:
        return redirect(url_for('main.profile'))
    
    form = OnboardingStep1Form()
    
    # Prepopulate from session
    if request.method == 'GET' and 'onboarding' in session:
        form.name.data = session['onboarding'].get('name')
        form.age.data = session['onboarding'].get('age')
        form.dependents.data = session['onboarding'].get('dependents', 0)
    
    if form.validate_on_submit():
        if 'onboarding' not in session:
            session['onboarding'] = {}
        
        session['onboarding']['name'] = form.name.data
        session['onboarding']['age'] = form.age.data
        session['onboarding']['dependents'] = form.dependents.data or 0
        session.modified = True
        
        return redirect(url_for('main.onboarding_step2'))
    
    return render_template('onboarding/step1_personal.html', form=form, step=1)


@main_bp.route('/onboarding/step2', methods=['GET', 'POST'])
@login_required
def onboarding_step2():
    """Step 2: Financial Information"""
    if current_user.profile:
        return redirect(url_for('main.profile'))
    
    # Ensure step 1 is completed
    if 'onboarding' not in session or 'name' not in session['onboarding']:
        flash('Please complete step 1 first.', 'warning')
        return redirect(url_for('main.onboarding_step1'))
    
    form = OnboardingStep2Form()
    
    if request.method == 'GET':
        form.investment_amount.data = session['onboarding'].get('investment_amount')
        form.annual_income.data = session['onboarding'].get('annual_income')
        form.expected_return.data = session['onboarding'].get('expected_return')
        form.total_debt.data = session['onboarding'].get('total_debt', 0)
    
    if form.validate_on_submit():
        session['onboarding']['investment_amount'] = form.investment_amount.data
        session['onboarding']['annual_income'] = form.annual_income.data
        session['onboarding']['expected_return'] = form.expected_return.data
        session['onboarding']['total_debt'] = form.total_debt.data or 0
        session.modified = True
        
        return redirect(url_for('main.onboarding_step3'))
    
    return render_template('onboarding/step2_financial.html', form=form, step=2)


@main_bp.route('/onboarding/step3', methods=['GET', 'POST'])
@login_required
def onboarding_step3():
    """Step 3: Investment Preferences"""
    if current_user.profile:
        return redirect(url_for('main.profile'))
    
    if 'onboarding' not in session or 'investment_amount' not in session['onboarding']:
        flash('Please complete step 2 first.', 'warning')
        return redirect(url_for('main.onboarding_step2'))
    
    form = OnboardingStep3Form()
    
    if request.method == 'GET':
        form.risk_preference.data = session['onboarding'].get('risk_preference')
        form.investment_goals.data = session['onboarding'].get('investment_goals')
        form.industry_interest.data = session['onboarding'].get('industry_interest', [])
    
    if form.validate_on_submit():
        session['onboarding']['risk_preference'] = form.risk_preference.data
        session['onboarding']['investment_goals'] = form.investment_goals.data
        session['onboarding']['industry_interest'] = form.industry_interest.data
        session.modified = True
        
        return redirect(url_for('main.onboarding_step4'))
    
    return render_template('onboarding/step3_preferences.html', form=form, step=3)


@main_bp.route('/onboarding/step4', methods=['GET', 'POST'])
@login_required
def onboarding_step4():
    """Step 4: Risk Assessment Questionnaire"""
    if current_user.profile:
        return redirect(url_for('main.profile'))
    
    if 'onboarding' not in session or 'risk_preference' not in session['onboarding']:
        flash('Please complete step 3 first.', 'warning')
        return redirect(url_for('main.onboarding_step3'))
    
    form = OnboardingStep4Form()
    
    if request.method == 'GET':
        answers = session['onboarding'].get('questionnaire_answers', {})
        form.q1.data = answers.get('q1')
        form.q2.data = answers.get('q2')
        form.q3.data = answers.get('q3')
        form.q4.data = answers.get('q4')
        form.q5.data = answers.get('q5')
    
    if form.validate_on_submit():
        session['onboarding']['questionnaire_answers'] = {
            'q1': form.q1.data,
            'q2': form.q2.data,
            'q3': form.q3.data,
            'q4': form.q4.data,
            'q5': form.q5.data
        }
        session.modified = True
        
        return redirect(url_for('main.onboarding_complete'))
    
    return render_template('onboarding/step4_questionnaire.html', form=form, step=4)


@main_bp.route('/onboarding/complete')
@login_required
def onboarding_complete():
    """Complete onboarding and save profile"""
    if current_user.profile:
        return redirect(url_for('main.profile'))
    
    if 'onboarding' not in session:
        flash('Please complete the onboarding process.', 'warning')
        return redirect(url_for('main.onboarding_step1'))
    
    # Get onboarding data and update user profile
    profile_data = session['onboarding']
    current_user.update_profile(profile_data)
    
    # Generate recommendations
    generate_recommendations(current_user)
    
    # Clear session data
    session.pop('onboarding', None)
    session.modified = True
    
    return render_template('onboarding/analysis.html')


@main_bp.route('/analysis')
@login_required
def analysis():
    """Analysis loading screen (redirects to recommendations)"""
    return render_template('onboarding/analysis.html')


# ==================== PROFILE ====================

@main_bp.route('/profile')
@login_required
def profile():
    """User profile page"""
    if not current_user.profile:
        flash('Please complete your profile first.', 'warning')
        return redirect(url_for('main.onboarding_step1'))
    
    # Convert profile dict to object-like for template compatibility
    class ProfileView:
        def __init__(self, data):
            for key, value in data.items():
                setattr(self, key, value)
    
    profile_obj = ProfileView(current_user.profile) if current_user.profile else None
    
    return render_template('profile.html', profile=profile_obj)


@main_bp.route('/profile/edit', methods=['POST'])
@login_required
def profile_edit():
    """AJAX endpoint for profile editing"""
    if not current_user.profile:
        return jsonify({'success': False, 'message': 'Profile not found'}), 404
    
    data = request.get_json()
    section = data.get('section')
    updates = data.get('updates', {})
    
    if not updates:
        return jsonify({'success': False, 'message': 'No updates provided'}), 400
    
    # Get current profile and update
    profile_data = dict(current_user.profile)
    
    # Apply updates based on section
    allowed_fields = {
        'personal': ['name', 'age', 'dependents'],
        'financial': ['investment_amount', 'annual_income', 'expected_return', 'total_debt'],
        'preferences': ['risk_preference', 'investment_goals']
    }
    
    for field in allowed_fields.get(section, []):
        if field in updates:
            value = updates[field]
            # Type conversion
            if field in ['age', 'dependents']:
                value = int(value) if value else 0
            elif field in ['investment_amount', 'expected_return', 'total_debt']:
                value = float(value) if value else 0
            profile_data[field] = value
    
    # Update profile (this recalculates risk score)
    current_user.update_profile(profile_data)
    
    # Regenerate recommendations if financial/preferences changed
    if section in ['financial', 'preferences']:
        generate_recommendations(current_user)
    
    return jsonify({'success': True, 'message': 'Profile updated successfully'})


# ==================== RECOMMENDATIONS ====================

@main_bp.route('/recommendations')
@login_required
def recommendations():
    """Recommendations dashboard"""
    if not current_user.profile:
        flash('Please complete your profile first.', 'warning')
        return redirect(url_for('main.onboarding_step1'))
    
    # Get recommendations
    stocks = StockRecommendation.get_by_user(current_user.get_id())
    fnos = FNORecommendation.get_by_user(current_user.get_id())
    
    # Calculate totals
    total_stock_investment = sum(s.allocation_amount for s in stocks)
    total_fno_investment = sum(f.premium * f.quantity for f in fnos)
    
    avg_stock_return = sum(s.expected_return for s in stocks) / len(stocks) if stocks else 0
    avg_fno_profit = sum(f.max_profit for f in fnos) / len(fnos) if fnos else 0
    
    return render_template('recommendations.html',
        stocks=stocks,
        fnos=fnos,
        total_stock_investment=total_stock_investment,
        total_fno_investment=total_fno_investment,
        avg_stock_return=avg_stock_return,
        avg_fno_profit=avg_fno_profit
    )


@main_bp.route('/recommendations/refresh', methods=['POST'])
@login_required
def refresh_recommendations():
    """AJAX endpoint to refresh recommendations"""
    if not current_user.profile:
        return jsonify({'success': False, 'message': 'Profile not found'}), 404
    
    try:
        generate_recommendations(current_user)
        return jsonify({'success': True, 'message': 'Recommendations refreshed'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500
