"""
Utility functions for generating recommendations
"""
from datetime import datetime, timedelta
from app.models import StockRecommendation, FNORecommendation


# Sample stock data for recommendations
SAMPLE_STOCKS = [
    {'symbol': 'RELIANCE', 'company_name': 'Reliance Industries', 'sector': 'Energy', 'base_price': 2450.0},
    {'symbol': 'TCS', 'company_name': 'Tata Consultancy Services', 'sector': 'Technology', 'base_price': 3890.0},
    {'symbol': 'HDFCBANK', 'company_name': 'HDFC Bank', 'sector': 'Finance', 'base_price': 1650.0},
    {'symbol': 'INFY', 'company_name': 'Infosys', 'sector': 'Technology', 'base_price': 1520.0},
    {'symbol': 'ICICIBANK', 'company_name': 'ICICI Bank', 'sector': 'Finance', 'base_price': 1025.0},
    {'symbol': 'SBIN', 'company_name': 'State Bank of India', 'sector': 'Finance', 'base_price': 620.0},
    {'symbol': 'BHARTIARTL', 'company_name': 'Bharti Airtel', 'sector': 'Telecom', 'base_price': 1180.0},
    {'symbol': 'ITC', 'company_name': 'ITC Limited', 'sector': 'FMCG', 'base_price': 455.0},
    {'symbol': 'WIPRO', 'company_name': 'Wipro Limited', 'sector': 'Technology', 'base_price': 485.0},
    {'symbol': 'SUNPHARMA', 'company_name': 'Sun Pharmaceutical', 'sector': 'Healthcare', 'base_price': 1420.0},
    {'symbol': 'TATAMOTORS', 'company_name': 'Tata Motors', 'sector': 'Manufacturing', 'base_price': 780.0},
    {'symbol': 'ADANIENT', 'company_name': 'Adani Enterprises', 'sector': 'Infrastructure', 'base_price': 2850.0},
    {'symbol': 'POWERGRID', 'company_name': 'Power Grid Corporation', 'sector': 'Energy', 'base_price': 285.0},
    {'symbol': 'NTPC', 'company_name': 'NTPC Limited', 'sector': 'Energy', 'base_price': 345.0},
    {'symbol': 'DRREDDY', 'company_name': 'Dr. Reddy\'s Laboratories', 'sector': 'Healthcare', 'base_price': 5620.0},
]

# Sector to industry mapping
SECTOR_MAP = {
    'technology': ['Technology'],
    'finance': ['Finance'],
    'healthcare': ['Healthcare'],
    'energy': ['Energy'],
    'fmcg': ['FMCG'],
    'manufacturing': ['Manufacturing'],
    'real_estate': ['Real Estate'],
    'infrastructure': ['Infrastructure', 'Telecom']
}


def generate_recommendations(user):
    """Generate stock and F&O recommendations based on user profile"""
    profile = user.profile
    if not profile:
        return
    
    # Clear existing recommendations
    StockRecommendation.delete_by_user(user.get_id())
    FNORecommendation.delete_by_user(user.get_id())
    
    investment_amount = profile.get('investment_amount', 100000)
    risk_score = profile.get('risk_score', 50)
    industries = profile.get('industry_interest', [])
    
    # Determine allocation split
    if risk_score >= 70:
        stock_percent = 0.6
        fno_percent = 0.4
    elif risk_score >= 40:
        stock_percent = 0.8
        fno_percent = 0.2
    else:
        stock_percent = 0.95
        fno_percent = 0.05
    
    stock_budget = investment_amount * stock_percent
    fno_budget = investment_amount * fno_percent
    
    # Filter stocks by preferred sectors
    preferred_sectors = []
    for ind in industries:
        preferred_sectors.extend(SECTOR_MAP.get(ind, []))
    
    available_stocks = [s for s in SAMPLE_STOCKS if s['sector'] in preferred_sectors] if preferred_sectors else SAMPLE_STOCKS
    
    if not available_stocks:
        available_stocks = SAMPLE_STOCKS[:5]
    
    # Select stocks based on risk profile
    num_stocks = 5 if risk_score >= 50 else 8
    selected_stocks = available_stocks[:min(num_stocks, len(available_stocks))]
    
    # Calculate allocations
    total_weight = sum(range(1, len(selected_stocks) + 1))
    
    for i, stock_data in enumerate(selected_stocks):
        weight = len(selected_stocks) - i
        allocation = stock_budget * (weight / total_weight)
        allocation_percent = (allocation / investment_amount) * 100
        
        # Calculate expected return based on risk
        base_return = 8 + (risk_score / 10)
        expected_return = base_return + (i * 0.5) - 2
        target_price = stock_data['base_price'] * (1 + expected_return / 100)
        
        # Determine risk level
        if i < 2:
            risk_level = 'high' if risk_score >= 50 else 'moderate'
        elif i < 4:
            risk_level = 'moderate'
        else:
            risk_level = 'low'
        
        StockRecommendation.create(user.get_id(), {
            'symbol': stock_data['symbol'],
            'company_name': stock_data['company_name'],
            'sector': stock_data['sector'],
            'current_price': stock_data['base_price'],
            'target_price': round(target_price, 2),
            'allocation_amount': round(allocation, 2),
            'allocation_percent': round(allocation_percent, 2),
            'expected_return': round(expected_return, 2),
            'risk_level': risk_level,
            'rationale': f'Selected based on your interest in {stock_data["sector"]} sector.'
        })
    
    # Generate F&O recommendations for higher risk profiles
    if risk_score >= 40 and fno_budget >= 10000:
        generate_fno_recommendations(user, fno_budget, risk_score, selected_stocks)


def generate_fno_recommendations(user, budget, risk_score, stocks):
    """Generate F&O recommendations"""
    expiry_date = datetime.now() + timedelta(days=30)
    expiry_date = expiry_date.replace(day=28)  # Last Thursday simulation
    
    # Number of F&O positions based on risk
    num_positions = 3 if risk_score >= 70 else 2 if risk_score >= 50 else 1
    position_budget = budget / num_positions
    
    for i in range(min(num_positions, len(stocks))):
        stock = stocks[i]
        base_price = stock['base_price']
        
        # Determine option type and position
        if risk_score >= 60:
            option_type = 'CALL'
            position = 'LONG'
            strike_price = base_price * 1.02  # 2% OTM
            premium = base_price * 0.03
        else:
            option_type = 'PUT'
            position = 'LONG'
            strike_price = base_price * 0.98  # 2% OTM
            premium = base_price * 0.025
        
        # Calculate quantity (lot size simulation)
        lot_size = 50 if base_price > 1000 else 100
        quantity = max(1, int(position_budget / (premium * lot_size))) * lot_size
        
        # Calculate P&L
        max_profit = base_price * 0.15 * quantity if position == 'LONG' else premium * quantity
        max_loss = premium * quantity if position == 'LONG' else base_price * 0.15 * quantity
        
        FNORecommendation.create(user.get_id(), {
            'symbol': stock['symbol'],
            'option_type': option_type,
            'position': position,
            'strike_price': round(strike_price, 2),
            'expiry': expiry_date,
            'premium': round(premium, 2),
            'quantity': quantity,
            'max_profit': round(max_profit, 2),
            'max_loss': round(max_loss, 2),
            'strategy_name': f'{option_type} {position}',
            'rationale': f'Based on your {stock["sector"]} sector interest and risk profile.'
        })
