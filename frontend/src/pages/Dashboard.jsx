import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import { stocksAPI } from '../services/api'
import StockCard from '../components/StockCard'
import SearchBar from '../components/SearchBar'
import './Dashboard.css'

function Dashboard() {
  const [stocks, setStocks] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')
  const [search, setSearch] = useState('')
  const [page, setPage] = useState(1)
  const [totalPages, setTotalPages] = useState(1)
  const navigate = useNavigate()

  useEffect(() => {
    loadStocks()
  }, [page, search])

  const loadStocks = async () => {
    setLoading(true)
    setError('')
    try {
      const response = await stocksAPI.getStocks(page, 12, search)
      setStocks(response.data.stocks)
      setTotalPages(response.data.pages)
    } catch (err) {
      setError('Failed to load stocks')
      setStocks([])
    } finally {
      setLoading(false)
    }
  }

  const handleSearch = (query) => {
    setSearch(query)
    setPage(1)
  }

  const handleStockClick = (ticker) => {
    navigate(`/stock/${ticker}`)
  }

  return (
    <div className="dashboard">
      <div className="container">
        <h1>Stock Market Dashboard</h1>

        <SearchBar onSearch={handleSearch} />

        {error && <div className="error">{error}</div>}

        {loading ? (
          <div className="loading">Loading stocks...</div>
        ) : stocks.length === 0 ? (
          <div className="no-data">No stocks found</div>
        ) : (
          <>
            <div className="stocks-grid">
              {stocks.map((stock) => (
                <StockCard
                  key={stock.id}
                  stock={stock}
                  onClick={() => handleStockClick(stock.ticker)}
                />
              ))}
            </div>

            <div className="pagination">
              <button onClick={() => setPage(p => Math.max(1, p - 1))} disabled={page === 1}>
                Previous
              </button>
              <span>Page {page} of {totalPages}</span>
              <button onClick={() => setPage(p => Math.min(totalPages, p + 1))} disabled={page === totalPages}>
                Next
              </button>
            </div>
          </>
        )}
      </div>
    </div>
  )
}

export default Dashboard
