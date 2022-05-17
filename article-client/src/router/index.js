import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieList from '@/views/MovieList'
import MyMovieList from '@/views/MyMovieList'
import RandomMovieList from '@/views/RandomMovieList'
import CommmunityView from '@/views/CommunityView'

Vue.use(VueRouter)

const routes = [
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
    path: '/community',
    name: 'community',
    component: CommmunityView
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
