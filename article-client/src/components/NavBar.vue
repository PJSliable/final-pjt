<template>
  <nav class="">
    <div class="mt-5 border-solid border-2 border-sky-400">
      <div class="title">
        <p>🥇Recommend Movie</p>
      </div>
    </div>
    <div class="mt-5 flex justify-between">
      <div clss="flex items-center">
        <router-link v-if="isLoggedIn" :to="{ name: 'movie' }">movie</router-link>
        <router-link v-if="isLoggedIn" :to="{ name: 'community' }">Community</router-link>
        <router-link v-if="isLoggedIn" :to="{ name: 'profile', params: { username } }"> 내 프로필</router-link>
        <router-link v-else :to="{ name: 'home' }">Home</router-link>
      </div>
      <div class="accounts">
        <div v-if="isLoggedIn">
          <router-link :to="{ name: 'logout' }">Logout</router-link>
        </div>
        <div v-else>
          <router-link :to="{ name: 'login'}">Login</router-link>
          <router-link :to="{ name: 'signup' }">Signup</router-link>
        </div>
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
  },
}
</script>

<style scoped>
nav {
  padding: 30px;
}

.title p {
  font-weight: bold;
  font-size: 50px;
}

nav a {
  font-weight: bold;
  color: #6e2583;
  padding: 10px 30px;
  border: 2px solid rgb(92, 44, 44);
  border-radius: 5%;
}

nav a.router-link-exact-active {
  color: #b439ed;
}
</style>