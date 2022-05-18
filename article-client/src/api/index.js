import axios from 'axios'

const API_BASE_URL = 'http://localhost:8000'
const LOGIN_URL = '/accounts/login/'
const SIGNUP_URL = '/accounts/signup/'

const login = async (body) => {
  const response = await axios.post(API_BASE_URL+LOGIN_URL, body)
  return response
}

const signup = async (body) => {
  const response = await axios.post(API_BASE_URL+SIGNUP_URL, body)
  return response
}


export {
  login,
  signup,
}