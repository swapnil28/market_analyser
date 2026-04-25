import { useState, useEffect } from 'react'
import { portfolioAPI } from '../services/api'
import './Portfolio.css'

function Portfolio() {
  const [portfolios, setPortfolios] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    loadPortfolios()
  }, [])

  const loadPortfolios = async () => {
    setLoading(true)
    setError('')
    try {
      const response = await portfolioAPI.getPortfolios()
      setPortfolios(response.data.portfolios)
    } catch (err) {
      setError('Failed to load portfolios')
    } finally {
      setLoading(false)
    }
  }

  if (loading) {
    return <div className="loading">Loading...</div>
  }

  return (
    <div className="portfolio">
      <div className="container">
        <h1>My Portfolios</h1>

        {error && <div className="error">{error}</div>}

        {portfolios.length === 0 ? (
          <div className="no-data">No portfolios yet. Create one to get started!</div>
        ) : (
          <div className="portfolios-grid">
            {portfolios.map((portfolio) => (
              <div key={portfolio.id} className="portfolio-card">
                <h3>{portfolio.name}</h3>
                {portfolio.description && <p>{portfolio.description}</p>}
                <div className="portfolio-stats">
                  <div>
                    <span className="label">Total Value:</span>
                    <span className="value">₹{portfolio.total_value.toFixed(2)}</span>
                  </div>
                  <div>
                    <span className="label">Holdings:</span>
                    <span className="value">{portfolio.holdings.length}</span>
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  )
}

export default Portfolio
