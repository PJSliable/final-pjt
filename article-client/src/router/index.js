import Vue from 'vue'
import VueRouter from 'vue-router'
import SignupView from '@/views/SignupView'
import LoginView from '@/views/LoginView'
import MovieView from '@/views/MovieView'
import MyMovieView from '@/views/MyMovieView'
import RecommendedView from '@/views/RecommendedView'
import CommmunityView from '@/views/CommunityView'
import DetailView from '@/views/DetailView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/signup',
    name: 'signup',
    component: SignupView,
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
  },
  {
    path: '/movies',
    name: 'movies',
    component: MovieView
  },
  {
    path: '/mine',
    name: 'mine',
    component: MyMovieView
  },
  {
    path: '/recommendation',
    name: 'recommendation',
    component: RecommendedView
  },
  {
    path: '/community',
    name: 'community',
    component: CommmunityView
  },
  {
    path: '/detail/:moviePk',
    name: 'detail',
    component: DetailView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
