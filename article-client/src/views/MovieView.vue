<template>
  <div>
    <p>모든 카드 보여주기</p>
    <div class="flex justify-end">
      <SearchForm/>
    </div>
    <div v-if="isObjEmpty">
      검색영화
      <SearchMovieList/>
    </div>
    <div v-else>
      <MovieList
        v-for="movieData in movies"
        :key="movieData.genre"
        :movieList="movieData.data"
        :genre="movieData.genre"
      />
    </div>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList.vue'
import SearchForm from '@/components/SearchForm.vue'
import SearchMovieList from '@/components/SearchMovieList.vue'

export default {
  name: 'MovieView',
  components: {
    MovieList,
    SearchForm,
    SearchMovieList,
  },
  computed: {
    movies() {
      return this.$store.state.movies.movies
    },
    isObjEmpty() {
      return Object.keys(this.$store.state.movies.searchMovies).length
    },
  },
  
  created() {
    this.$store.dispatch('clearMovies')
    this.$store.dispatch('fetchMovies')
  },
  mounted() {
  }
}
</script>

<style scoped>
.active {
  color: #42b983;
}

</style>