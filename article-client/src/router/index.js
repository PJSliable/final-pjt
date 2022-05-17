import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '@/views/MovieView'
import CommmunityView from '@/views/CommunityView'
import MovieList from '@/views/MovieList'
import MyMovieList from '@/views/MyMovieList'
import RandomMovieList from '@/views/RandomMovieList'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'movie',
    component: MovieView
  },
  {
    path: '/community',
    name: 'community',
    component: CommmunityView
  },
  {
    path: '/movies',
    name: 'movies',
    component: MovieList
  },
  {
    path: '/mine',
    name: 'mine',
    component: MyMovieList
  },
  {
    path: '/random',
    name: 'random',
    component: RandomMovieList
  },
  {
    path: '/detail/:moviePk',
    name: 'detail',
    component: RandomMovieList
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
