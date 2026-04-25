import axios from 'axios'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5001'

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Add token to requests
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => Promise.reject(error)
)

export const authAPI = {
  register: (email, password, firstName, lastName) =>
    api.post('/auth/register', { email, password, first_name: firstName, last_name: lastName }),
  login: (email, password) =>
    api.post('/auth/login', { email, password }),
  getCurrentUser: () =>
    api.get('/auth/me'),
}

export const stocksAPI = {
  getStocks: (page = 1, perPage = 20, search = '') =>
    api.get('/stocks', { params: { page, per_page: perPage, search } }),
  getStock: (ticker) =>
    api.get(`/stocks/${ticker}`),
  getStockPrices: (ticker, days = 30) =>
    api.get(`/stocks/${ticker}/prices`, { params: { days } }),
}

export const portfolioAPI = {
  getPortfolios: () =>
    api.get('/portfolio'),
  createPortfolio: (name, description) =>
    api.post('/portfolio', { name, description }),
  getPortfolio: (portfolioId) =>
    api.get(`/portfolio/${portfolioId}`),
  addHolding: (portfolioId, stockId, quantity, avgCost) =>
    api.post(`/portfolio/${portfolioId}/holdings`, { stock_id: stockId, quantity, avg_cost: avgCost }),
}

export const watchlistAPI = {
  getWatchlists: () =>
    api.get('/watchlist'),
  createWatchlist: (name, description) =>
    api.post('/watchlist', { name, description }),
  getWatchlist: (watchlistId) =>
    api.get(`/watchlist/${watchlistId}`),
  addItem: (watchlistId, stockId) =>
    api.post(`/watchlist/${watchlistId}/items`, { stock_id: stockId }),
}

export default api
