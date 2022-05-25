import axios from 'axios'
import _ from 'lodash'
import api from '@/api/index.js'

export default {
  state: {
    recommendMovies: [],
    movies: [],
    searchMovies: [],
    movieDetail: {},
    imageBaseUrl: "https://www.themoviedb.org/t/p/original",
    genres:{
      '12':'모험',
      '14':'판타지',
      '16':'애니메이션',
      '18':'드라마',
      '27':'공포',
      '28':'액션',
      '35':'코미디',
      '36':'역사',
      '37':'서부',
      '53':'스릴러',
      '80':'범죄',
      '99':'다큐멘터리',
      '878':'SF',
      '9648':'미스터리',
      '10402':'음악',
      '10749':'로맨스',
      '10751':'가족',
      '10752':'전쟁',
      '10770':'TV',
      },
  },
  getters: {
    genres: state => state.genres,
    backdropImg: state => state.movieDetail.backdrop_path,
  },
  mutations: {
    CLEAR_MOVIES(state) {
      state.movies = []
      state.recommendMovies = []
      state.searchMovies = []
    },
    FETCH_RECOMMEND_MOVIES(state, movies) {
      state.recommendMovies = movies
    },
    FETCH_MOVIES(state, movies) {
      state.movies.push(movies)
    },
    FETCH_MOVIE_DETAIL(state, movieDetail) {
      state.movieDetail = movieDetail
    },
    FETCH_SEARCH_MOVIES(state, searchMovies) {
      state.searchMovies = searchMovies
    },
  },
  actions: {
    clearMovies({commit}) {
      commit('CLEAR_MOVIES')
    },
    fetchRecommedMovies({ commit, getters }) {
      axios({
        url: api.movies.recommends(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('FETCH_RECOMMEND_MOVIES', res.data)
        })
    },
    fetchMovies({ commit }) {
      const genres = [12, 14, 16, 18, 27, 28, 35, 36, 37, 53, 80, 99, 878, 9648, 10402, 10749, 10751, 10752, 10770]
      const randomGenres = _.sampleSize(genres, 3)
      randomGenres.forEach((genre) => {
        axios({
          method: 'get',
          url: api.movies.movies(),
          params: {
            genre_id: genre
          }
        })
          .then((res) => {
            const movies = {
              genre: genre,
              data: res.data
            }
            commit('FETCH_MOVIES', movies)
          })
          .catch((err) => {
            console.log(err.res)
          })
      })
    },
    fetchDetail({ commit }, { moviePk }) {
      commit('FETCH_MOVIE_DETAIL', {})
      axios({
        url: api.movies.movieDetail(moviePk),
        method: 'get',
      })
        .then(res => {
          commit('FETCH_MOVIE_DETAIL', res.data)
        })
    },
    fetchSearchMovies({ commit }, userInput) {
      if (!userInput) {
        return commit('FETCH_SEARCH_MOVIES', [])
      }
      axios({
        url: api.movies.search(),
        method: 'get',
        params: {
          userInput : userInput
        },
      })
        .then(res => {
          if (res.status === 204) {
            return
          }
          commit('FETCH_SEARCH_MOVIES', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
    likeMovie({ getters }, moviePk) {
      axios({
        url: api.movies.like(),
        method: 'post',
        data: {
          moviePk
        },
        headers: getters.authHeader,
      })
    }
  },
}