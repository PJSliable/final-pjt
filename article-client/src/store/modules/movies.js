import axios from 'axios'
import _ from 'lodash'
import api from '@/api/index.js'

export default {
  state: {
    movies: [],
    searchMovies: [],
    movieDetail: {},
    imageBaseUrl: "https://www.themoviedb.org/t/p/original",
    genres: [12, 14, 16, 18, 27, 28, 35, 36, 37, 53, 80, 99, 878, 9648, 10402, 10749, 10751, 10752, 10770],
  },
  getters: {
  },
  mutations: {
    CLEAR_MOVIES(state) {
      state.movies = []
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
          console.log(res)
        })

    }
  },
}