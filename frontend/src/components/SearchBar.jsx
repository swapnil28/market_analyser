import { useState } from 'react'
import './SearchBar.css'

function SearchBar({ onSearch }) {
  const [query, setQuery] = useState('')

  const handleChange = (e) => {
    const value = e.target.value
    setQuery(value)
    onSearch(value)
  }

  return (
    <div className="search-bar">
      <input
        type="text"
        placeholder="Search by ticker or name..."
        value={query}
        onChange={handleChange}
        className="search-input"
      />
      <span className="search-icon">🔍</span>
    </div>
  )
}

export default SearchBar
