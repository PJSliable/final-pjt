import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '@/store'

import NotFound404 from '@/views/NotFound404.vue'

import SignupView from '@/views/accounts/SignupView.vue'
import LoginView from '@/views/accounts/LoginView.vue'
import LogoutView from '@/views/accounts/LogoutView.vue'
import ProfileView from '@/views/accounts/ProfileView.vue'

import HomeView from '@/views/HomeView.vue'
import MovieView from '@/views/MovieView.vue'
import DetailView from '@/views/DetailView.vue'

import CommmunityView from '@/views/community/CommunityView.vue'
import ReviewCreateView from '@/views/community/ReviewCreateView.vue'
import ReviewDetailView from '@/views/community/ReviewDetailView.vue'
import ReviewEditView from '@/views/community/ReviewEditView.vue'

import Swal from 'sweetalert2'

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
    path: '/logout',
    name: 'logout',
    component: LogoutView,
  },
  {
    path: '/profile/:username',
    name: 'profile',
    component: ProfileView,
  },
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/movie',
    name: 'movie',
    component: MovieView
  },
  {
    path: '/detail/:moviePk',
    name: 'detail',
    component: DetailView
  },
  {
    path: '/community',
    name: 'community',
    component: CommmunityView
  },
  {
    path: '/community/:moviePk/create',
    name: 'reviewCreate',
    component: ReviewCreateView,
  },
  {
    path: '/community/:reviewPk',
    name: 'reviewDetail',
    component: ReviewDetailView,
  },
  {
    path: '/community/:reviewPk/edit',
    name: 'reviewEdit',
    component: ReviewEditView
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect: '/404'
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  store.commit('SET_AUTH_ERROR', null)

  const { isLoggedIn } = store.getters
  const noAuthPages = ['home', 'login', 'signup']
  const isAuthRequired = !noAuthPages.includes(to.name)

  if (isAuthRequired && !isLoggedIn) {
    Swal.fire({
      icon: 'error',
      title: '비정상적인 접근',
      text: '다시 시도해주세요.'
    })
    next({ name: 'login' })
  } else if (!isAuthRequired && isLoggedIn) {
    next({ name: 'movie' })
  } else {
    next()
  }
})

export default router
