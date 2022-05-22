const API_BASE_URL = 'http://localhost:8000/'

const LOGIN_URL = 'accounts/login/'
const SIGNUP_URL = 'accounts/signup/'
const LOGOUT_URL = 'accounts/logout/'
const USER_URL = 'accounts/user/'
const PROFILE_URL = 'accounts/profile/'

const MOVIES_URL = 'movies/'
const SEARCH_URL = 'movies/search'

const COMMUNITY_URL = 'community/'
const COMMENT_URL = 'comment/'

export default {
  accounts: {
    login: () => API_BASE_URL + LOGIN_URL,
    logout: () => API_BASE_URL + LOGOUT_URL,
    signup: () => API_BASE_URL + SIGNUP_URL,
    currentUserInfo: () => API_BASE_URL + USER_URL,
    profile: username => API_BASE_URL + PROFILE_URL + username,
  },
  community: {
    reviews: () => API_BASE_URL + COMMUNITY_URL,
    review: reviewPk => API_BASE_URL + COMMUNITY_URL + `${reviewPk}/`,
  //   likeArticle: articlePk => HOST + ARTICLES + `${articlePk}/` + 'like/',
    comments: commentPk => API_BASE_URL + COMMUNITY_URL + COMMENT_URL + `${commentPk}/`,
    comment: () => API_BASE_URL + COMMUNITY_URL + COMMENT_URL,
  },
  movies: {
    movies: () => API_BASE_URL + MOVIES_URL,
    movieDetail: moviePk =>API_BASE_URL + MOVIES_URL + `${moviePk}/`,
    search: () => API_BASE_URL + SEARCH_URL
  }
}