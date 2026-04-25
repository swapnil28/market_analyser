from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.user import User
from app.models.portfolio import Portfolio
from app.models.holding import PortfolioHolding
from app.models.stock import Stock
from app import db

portfolio_bp = Blueprint('portfolio', __name__, url_prefix='/portfolio')


@portfolio_bp.route('', methods=['GET'])
@jwt_required()
def get_portfolios():
    """Get user's portfolios."""
    user_id = get_jwt_identity()
    portfolios = Portfolio.query.filter_by(user_id=user_id).all()

    return jsonify({
        'portfolios': [p.to_dict() for p in portfolios],
    }), 200


@portfolio_bp.route('', methods=['POST'])
@jwt_required()
def create_portfolio():
    """Create a new portfolio."""
    user_id = get_jwt_identity()
    data = request.get_json()

    if not data or not data.get('name'):
        return jsonify({'error': 'Portfolio name required'}), 400

    portfolio = Portfolio(
        user_id=user_id,
        name=data['name'],
        description=data.get('description'),
    )

    db.session.add(portfolio)
    db.session.commit()

    return jsonify({'portfolio': portfolio.to_dict()}), 201


@portfolio_bp.route('/<int:portfolio_id>', methods=['GET'])
@jwt_required()
def get_portfolio(portfolio_id):
    """Get a specific portfolio."""
    user_id = get_jwt_identity()
    portfolio = Portfolio.query.filter_by(id=portfolio_id, user_id=user_id).first()

    if not portfolio:
        return jsonify({'error': 'Portfolio not found'}), 404

    return jsonify({'portfolio': portfolio.to_dict()}), 200


@portfolio_bp.route('/<int:portfolio_id>/holdings', methods=['POST'])
@jwt_required()
def add_holding(portfolio_id):
    """Add a stock holding to portfolio."""
    user_id = get_jwt_identity()
    portfolio = Portfolio.query.filter_by(id=portfolio_id, user_id=user_id).first()

    if not portfolio:
        return jsonify({'error': 'Portfolio not found'}), 404

    data = request.get_json()

    if not data or not data.get('stock_id') or not data.get('quantity') or not data.get('avg_cost'):
        return jsonify({'error': 'stock_id, quantity, and avg_cost required'}), 400

    stock = Stock.query.get(data['stock_id'])
    if not stock:
        return jsonify({'error': 'Stock not found'}), 404

    holding = PortfolioHolding(
        portfolio_id=portfolio_id,
        stock_id=data['stock_id'],
        quantity=float(data['quantity']),
        avg_cost=float(data['avg_cost']),
    )

    db.session.add(holding)
    db.session.commit()

    return jsonify({'holding': holding.to_dict()}), 201
