from flask import Blueprint, request, jsonify
from app.models.stock import Stock
from app.models.price import Price
from app import db

stocks_bp = Blueprint('stocks', __name__, url_prefix='/stocks')


@stocks_bp.route('', methods=['GET'])
def get_stocks():
    """Get all stocks with pagination."""
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    search = request.args.get('search', '', type=str)

    query = Stock.query

    if search:
        query = query.filter(
            (Stock.ticker.ilike(f'%{search}%')) |
            (Stock.name.ilike(f'%{search}%'))
        )

    paginated = query.paginate(page=page, per_page=per_page, error_out=False)

    return jsonify({
        'stocks': [stock.to_dict() for stock in paginated.items],
        'total': paginated.total,
        'pages': paginated.pages,
        'current_page': page,
    }), 200


@stocks_bp.route('/<ticker>', methods=['GET'])
def get_stock(ticker):
    """Get a specific stock by ticker."""
    stock = Stock.query.filter_by(ticker=ticker.upper()).first()

    if not stock:
        return jsonify({'error': 'Stock not found'}), 404

    return jsonify({'stock': stock.to_dict()}), 200


@stocks_bp.route('/<ticker>/prices', methods=['GET'])
def get_stock_prices(ticker):
    """Get price history for a stock."""
    days = request.args.get('days', 30, type=int)

    stock = Stock.query.filter_by(ticker=ticker.upper()).first()

    if not stock:
        return jsonify({'error': 'Stock not found'}), 404

    prices = Price.query.filter_by(stock_id=stock.id).order_by(
        Price.date.desc()
    ).limit(days).all()

    return jsonify({
        'ticker': stock.ticker,
        'name': stock.name,
        'prices': [price.to_dict() for price in reversed(prices)],
    }), 200
