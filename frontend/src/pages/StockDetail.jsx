import { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'
import { stocksAPI } from '../services/api'
import PriceChart from '../components/PriceChart'
import './StockDetail.css'

function StockDetail() {
  const { ticker } = useParams()
  const [stock, setStock] = useState(null)
  const [prices, setPrices] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    loadStockData()
  }, [ticker])

  const loadStockData = async () => {
    setLoading(true)
    setError('')
    try {
      const stockRes = await stocksAPI.getStock(ticker)
      setStock(stockRes.data.stock)

      const pricesRes = await stocksAPI.getStockPrices(ticker)
      setPrices(pricesRes.data.prices)
    } catch (err) {
      setError('Failed to load stock data')
    } finally {
      setLoading(false)
    }
  }

  if (loading) {
    return <div className="loading">Loading...</div>
  }

  if (error) {
    return <div className="error">{error}</div>
  }

  if (!stock) {
    return <div className="error">Stock not found</div>
  }

  return (
    <div className="stock-detail">
      <div className="container">
        <div className="stock-header">
          <h1>{stock.ticker} - {stock.name}</h1>
          <p className="exchange">{stock.exchange}</p>
          <div className="price-display">
            <span className="current-price">₹{stock.current_price.toFixed(2)}</span>
          </div>
        </div>

        {prices.length > 0 && (
          <div className="chart-container">
            <PriceChart prices={prices} ticker={stock.ticker} />
          </div>
        )}

        {prices.length > 0 && (
          <table className="prices-table">
            <thead>
              <tr>
                <th>Date</th>
                <th>Open</th>
                <th>High</th>
                <th>Low</th>
                <th>Close</th>
                <th>Volume</th>
              </tr>
            </thead>
            <tbody>
              {prices.map((price) => (
                <tr key={price.id}>
                  <td>{price.date}</td>
                  <td>₹{price.open.toFixed(2)}</td>
                  <td>₹{price.high.toFixed(2)}</td>
                  <td>₹{price.low.toFixed(2)}</td>
                  <td>₹{price.close.toFixed(2)}</td>
                  <td>{(price.volume / 1000000).toFixed(2)}M</td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </div>
  )
}

export default StockDetail
