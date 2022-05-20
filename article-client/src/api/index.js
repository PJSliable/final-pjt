const API_BASE_URL = 'http://localhost:8000/'
const LOGIN_URL = 'accounts/login/'
const SIGNUP_URL = 'accounts/signup/'
const LOGOUT_URL = 'accounts/logout/'
const USER_URL = 'accounts/user/'
const PROFILE_URL = 'accounts/profile/'

const MOVIES_URL = 'movies/'

const REVIEWS_URL = 'community/'

export default {
  accounts: {
    login: () => API_BASE_URL + LOGIN_URL,
    logout: () => API_BASE_URL + LOGOUT_URL,
    signup: () => API_BASE_URL + SIGNUP_URL,
    currentUserInfo: () => API_BASE_URL + USER_URL,
    profile: username => API_BASE_URL +PROFILE_URL + username,
  },
  reviews: {
    reviews: () => API_BASE_URL + REVIEWS_URL,
    review: reviewPk => API_BASE_URL + REVIEWS_URL + `${reviewPk}/`,
  //   likeArticle: articlePk => HOST + ARTICLES + `${articlePk}/` + 'like/',
  //   comments: articlePk => HOST + ARTICLES + `${articlePk}/` + COMMENTS,
  //   comment: (articlePk, commentPk) =>
  //     HOST + ARTICLES + `${articlePk}/` + COMMENTS + `${commentPk}/`,
  },
  movies: {
    movies: () => API_BASE_URL + MOVIES_URL,
    movieDetail: moviePk =>API_BASE_URL + MOVIES_URL + moviePk,
  }
}