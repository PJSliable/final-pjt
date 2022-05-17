<template>
  <div id="app">
    <div class="mt-5 border-solid border-2 border-sky-400">
      <div class="title">
        <p>🥇Recommend Movie</p>
      </div>
    </div>
    <br>
    <nav class="flex justify-around">
      <router-link :to="{ name: 'movies' }">Total</router-link>
      <router-link :to="{ name: 'mine' }">Mine</router-link>
      <router-link :to="{ name: 'random' }">Random</router-link>
      <router-link :to="{ name: 'community' }">Community</router-link>
    </nav>
    <br>
    <br>
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

.title p {
  font-weight: bold;
  font-size: 50px;
}

nav a {
  font-weight: bold;
  color: #321d71;
  padding: 10px 30px;
  border: 2px solid black;
  border-radius: 5%;
}

nav a.router-link-exact-active {
  color: #b439ed;
}
</style>
