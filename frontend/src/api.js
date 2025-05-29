import axios from 'axios';

const api = axios.create({
  baseURL: 'https://expense-tracker-backend-seven-gamma.vercel.app'
});

export default api;
