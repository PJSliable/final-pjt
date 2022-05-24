<template>
  <div>
    <div class="flex flex-col md:flex-row  md:justify-between">
      <div class="p-5 ml-5 mt-4 text-2xl md:text-4xl font-bold font-DoHyeon">
        <div v-if="isObjEmpty">
          <p>Search</p>
        </div>
        <div v-else>
          <p>Movie List</p>
        </div>
      </div>
      <div class="flex justify-center md:mt-5 items-center">
        <SearchForm/>
      </div>
    </div>
    <div v-if="isObjEmpty">
      
      <SearchMovieList/>
    </div>
    <div v-else>
      <div >
        
      </div>
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

.font-sans {
  font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
}
</style>