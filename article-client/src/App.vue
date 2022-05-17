<template>
  <div id="app">
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',
  created() {
    const API_LOGIN_URL = 'http://localhost:8000/dj-rest-auth/login'
    // const API_ARTICLE_LIST = '/articles/'

    axios.post(API_LOGIN_URL,
    {
      username:'12345',
      password:'123456789!',
      email:'jongsun199@gmail.com',
    }
    )
    .then(
      res => {
        console.log(res)
      }
    )
    .catch(
      err => {
        // 추후 상태코드에 따라 처리 
        console.error(err)
      }
    )
  },
  components: {

  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
