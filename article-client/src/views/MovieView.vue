<template>
  <div>
    <p>모든 카드 보여주기</p>
    <MovieList/>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList.vue'


export default {
  name: 'MovieView',
  components: {
    MovieList,
  },
  created() {
    this.$store.dispatch('clearMovies')
  },
  mounted() {
    this.$store.dispatch('fetchMovies')
  }
}
</script>

<style scoped>
.active {
  color: #42b983;
}
</style>