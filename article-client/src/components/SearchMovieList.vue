<template>
  <div>
    <div class="flex flex-wrap">
      <MovieCard
        v-for="(movie, index) in movieList"
        :key="index"
        :movie="movie"
      />
    </div>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard.vue'

export default {
  name: 'SearchMovieList',
  components: {
    MovieCard,
  },
  computed: {
    movieList() {
      return this.$store.state.movies.searchMovies
    }
  }
}
</script>

<style scoped>

</style>