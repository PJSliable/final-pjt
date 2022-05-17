<template>
  <div>
    <div>
      <router-link :to="{ name: 'movies' }">Total</router-link> |
      <router-link class="active" :to="{ name: 'mine' }">Mine</router-link> |
      <router-link :to="{ name: 'random' }">Random</router-link>
    </div>
    <p>내 카드 보여주기</p>
    <MovieCard/>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard.vue'


export default {
  name: 'MyMovieList',
  components: {
    MovieCard,
  },
}
</script>

<style scoped>
.active {
  color: #42b983;
}
</style>