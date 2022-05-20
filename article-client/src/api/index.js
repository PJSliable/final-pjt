const API_BASE_URL = 'http://localhost:8000/'
const LOGIN_URL = 'accounts/login/'
const SIGNUP_URL = 'accounts/signup/'
const LOGOUT_URL = 'accounts/logout/'
const USER_URL = 'accounts/user/'
const PROFILE_URL = 'accounts/profile/'

const MOVIES_URL = 'movies/'

export default {
  accounts: {
    login: () => API_BASE_URL + LOGIN_URL,
    logout: () => API_BASE_URL + LOGOUT_URL,
    signup: () => API_BASE_URL + SIGNUP_URL,
    currentUserInfo: () => API_BASE_URL + USER_URL,
    profile: username => API_BASE_URL +PROFILE_URL + username,
  },
  // articles: {
  //   articles: () => HOST + ARTICLES,
  //   article: articlePk => HOST + ARTICLES + `${articlePk}/`,
  //   likeArticle: articlePk => HOST + ARTICLES + `${articlePk}/` + 'like/',
  //   comments: articlePk => HOST + ARTICLES + `${articlePk}/` + COMMENTS,
  //   comment: (articlePk, commentPk) =>
  //     HOST + ARTICLES + `${articlePk}/` + COMMENTS + `${commentPk}/`,
  // },
  movies: {
    movies: () => API_BASE_URL + MOVIES_URL,
    movieDetail: moviePk =>API_BASE_URL + MOVIES_URL + moviePk,
  }
}