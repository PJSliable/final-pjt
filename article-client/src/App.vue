<template>
  <div id="app">
    <div class="flex justify-center mt-5">
      <nav class="border-solid border-2 border-sky-500 w-1/2">
        <p>Movie Recommend Site</p>
        <br>
        <router-link :to="{ name: 'movies' }">Total</router-link> |
        <router-link :to="{ name: 'mine' }">Mine</router-link> |
        <router-link :to="{ name: 'random' }">Random</router-link> |
        <router-link :to="{ name: 'community' }">Community</router-link>
      </nav>
    </div>
    <hr>
    <router-view/>
  </div>
</template>
<script>
export default{
  name: 'App',
}

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
