from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.user import User
from app.models.watchlist import Watchlist
from app.models.watchlist_item import WatchlistItem
from app.models.stock import Stock
from app import db

watchlist_bp = Blueprint('watchlist', __name__, url_prefix='/watchlist')


@watchlist_bp.route('', methods=['GET'])
@jwt_required()
def get_watchlists():
    """Get user's watchlists."""
    user_id = get_jwt_identity()
    watchlists = Watchlist.query.filter_by(user_id=user_id).all()

    return jsonify({
        'watchlists': [w.to_dict() for w in watchlists],
    }), 200


@watchlist_bp.route('', methods=['POST'])
@jwt_required()
def create_watchlist():
    """Create a new watchlist."""
    user_id = get_jwt_identity()
    data = request.get_json()

    if not data or not data.get('name'):
        return jsonify({'error': 'Watchlist name required'}), 400

    watchlist = Watchlist(
        user_id=user_id,
        name=data['name'],
        description=data.get('description'),
    )

    db.session.add(watchlist)
    db.session.commit()

    return jsonify({'watchlist': watchlist.to_dict()}), 201


@watchlist_bp.route('/<int:watchlist_id>', methods=['GET'])
@jwt_required()
def get_watchlist(watchlist_id):
    """Get a specific watchlist."""
    user_id = get_jwt_identity()
    watchlist = Watchlist.query.filter_by(id=watchlist_id, user_id=user_id).first()

    if not watchlist:
        return jsonify({'error': 'Watchlist not found'}), 404

    return jsonify({'watchlist': watchlist.to_dict()}), 200


@watchlist_bp.route('/<int:watchlist_id>/items', methods=['POST'])
@jwt_required()
def add_watchlist_item(watchlist_id):
    """Add a stock to watchlist."""
    user_id = get_jwt_identity()
    watchlist = Watchlist.query.filter_by(id=watchlist_id, user_id=user_id).first()

    if not watchlist:
        return jsonify({'error': 'Watchlist not found'}), 404

    data = request.get_json()

    if not data or not data.get('stock_id'):
        return jsonify({'error': 'stock_id required'}), 400

    stock = Stock.query.get(data['stock_id'])
    if not stock:
        return jsonify({'error': 'Stock not found'}), 404

    # Check if already in watchlist
    existing = WatchlistItem.query.filter_by(
        watchlist_id=watchlist_id,
        stock_id=data['stock_id']
    ).first()

    if existing:
        return jsonify({'error': 'Stock already in watchlist'}), 400

    item = WatchlistItem(
        watchlist_id=watchlist_id,
        stock_id=data['stock_id'],
    )

    db.session.add(item)
    db.session.commit()

    return jsonify({'item': item.to_dict()}), 201
