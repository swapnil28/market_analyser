import { useState, useEffect } from 'react'
import { watchlistAPI } from '../services/api'
import './Watchlist.css'

function Watchlist() {
  const [watchlists, setWatchlists] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState('')

  useEffect(() => {
    loadWatchlists()
  }, [])

  const loadWatchlists = async () => {
    setLoading(true)
    setError('')
    try {
      const response = await watchlistAPI.getWatchlists()
      setWatchlists(response.data.watchlists)
    } catch (err) {
      setError('Failed to load watchlists')
    } finally {
      setLoading(false)
    }
  }

  if (loading) {
    return <div className="loading">Loading...</div>
  }

  return (
    <div className="watchlist">
      <div className="container">
        <h1>My Watchlists</h1>

        {error && <div className="error">{error}</div>}

        {watchlists.length === 0 ? (
          <div className="no-data">No watchlists yet. Create one to track stocks!</div>
        ) : (
          <div className="watchlists-grid">
            {watchlists.map((watchlist) => (
              <div key={watchlist.id} className="watchlist-card">
                <h3>{watchlist.name}</h3>
                {watchlist.description && <p>{watchlist.description}</p>}
                <div className="items-count">
                  <span>{watchlist.items.length} items</span>
                </div>
                {watchlist.items.length > 0 && (
                  <ul className="items-list">
                    {watchlist.items.map((item) => (
                      <li key={item.id}>
                        {item.stock?.ticker} - {item.stock?.name}
                      </li>
                    ))}
                  </ul>
                )}
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  )
}

export default Watchlist
