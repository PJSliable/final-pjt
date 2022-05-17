<template>
  <div>
    <div>
      <router-link :to="{ name: 'movies' }">Total</router-link> |
      <router-link :to="{ name: 'mine' }">Mine</router-link> |
      <router-link class="active" :to="{ name: 'random' }">Random</router-link>
    </div>
    <p>랜덤 카드 보여주기</p>
    <MovieCard/>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard.vue'

export default {
  name: 'RandomMovieList',
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