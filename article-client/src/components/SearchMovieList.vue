<template>
  <div>
    <div class="w-full h-full grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 place-content-center">
      <MovieCard
        v-for="(movie, index) in movieList"
        :key="index"
        :movie="movie"
        :isLiked="false"
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
    },
  }
}
</script>

<style scoped>

</style>