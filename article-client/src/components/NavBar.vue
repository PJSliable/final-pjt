<template>
  <nav
    class="w-full border-b-2 rounded-b-md border-white flex flex-wrap items-center justify-between bg-white shadow-lg navbar navbar-expand-lg navbar-light"
  >
    <div class="container-fluid w-full flex flex-wrap items-center justify-between px-6 text-l text-white pr-2 font-semibold">
      <!-- 로고로 변경 필-->
      <router-link v-if="isLoggedIn" class="logo text-4xl text-white pr-2 font-semibold font-DoHyeon" :to="{ name: 'movie' }">GGM</router-link>
      <router-link  v-else class="logo text-4xl text-white pr-2 font-semibold font-DoHyeon"  :to="{ name: 'home' }">GGM</router-link>

      <button
        class="navbar-toggler text-gray-200 border-0 hover:shadow-none hover:no-underline py-2 px-2.5 bg-transparent focus:outline-none focus:ring-0 focus:shadow-none focus:no-underline"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent1"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <svg
          aria-hidden="true"
          focusable="false"
          data-prefix="fas"
          data-icon="bars"
          class="w-6"
          role="img"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 448 512"
        >
          <path
            fill="currentColor"
            d="M16 132h416c8.837 0 16-7.163 16-16V76c0-8.837-7.163-16-16-16H16C7.163 60 0 67.163 0 76v40c0 8.837 7.163 16 16 16zm0 160h416c8.837 0 16-7.163 16-16v-40c0-8.837-7.163-16-16-16H16c-8.837 0-16 7.163-16 16v40c0 8.837 7.163 16 16 16zm0 160h416c8.837 0 16-7.163 16-16v-40c0-8.837-7.163-16-16-16H16c-8.837 0-16 7.163-16 16v40c0 8.837 7.163 16 16 16z"
          ></path>
        </svg>
      </button>
      
      <div class="collapse navbar-collapse flex-grow items-center" id="navbarSupportedContent1">
        <ul class="navbar-nav flex flex-col pl-0 list-style-none mr-auto">
          <li class="nav-item p-2">
            <router-link class="nav-link font-DoHyeon text-xl" v-if="isLoggedIn" :to="{ name: 'movie' }">Movie</router-link>
          </li>
          <li v-if="isLoggedIn" class="nav-item p-2">
            <router-link :to="{ name: 'community' }" class="nav-link font-DoHyeon text-xl">Community</router-link>
          </li>
        </ul>

        <ul class="navbar-nav flex flex-col pr-0 list-style-none mr-0">
          <li class="nav-item p-2">
            <router-link v-if="isLoggedIn" :to="{ name: 'profile', params: { nickname } }" class="nav-link font-DoHyeon text-xl">My Profile</router-link>
            <router-link v-else class="nav-link" :to="{ name: 'login'}">Login</router-link>
          </li>
          <li class="nav-item p-2">
            <router-link v-if="isLoggedIn" class="nav-link font-DoHyeon text-xl" :to="{ name: 'logout' }">Logout</router-link>
            <router-link v-else class="nav-link" :to="{ name: 'signup' }">Signup</router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'NavBar',
  computed: {
    ...mapGetters(['isLoggedIn', 'currentUser']),
    username() {
      return this.currentUser.username ? this.currentUser.username : 'guest'
    },
    nickname() {
      return this.currentUser.nickname ? this.currentUser.nickname : 'guest'
    },
  },
}
</script>

<style scoped>
nav {
  padding: 20px;
}

.logo {
  color: black
}
.logo:hover {
  color: black
}
nav .logo.router-link-exact-active {
  color: black
}

.nav-link {
  color: black
}

.nav-link:hover{
  color: #c5c5c5
}

nav a.router-link-exact-active {
  font-weight: bold;
  color: #c5c5c5
}
</style>