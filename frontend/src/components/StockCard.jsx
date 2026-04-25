import './StockCard.css'

function StockCard({ stock, onClick }) {
  return (
    <div className="stock-card" onClick={onClick}>
      <div className="card-header">
        <h3>{stock.ticker}</h3>
        <span className="exchange">{stock.exchange}</span>
      </div>
      <p className="card-name">{stock.name}</p>
      <div className="card-price">
        <span className="price">₹{stock.current_price.toFixed(2)}</span>
      </div>
      <div className="card-footer">
        <button className="view-btn">View Details</button>
      </div>
    </div>
  )
}

export default StockCard
