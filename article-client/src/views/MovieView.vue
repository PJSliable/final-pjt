<template>
  <div>
    <p>모든 카드 보여주기</p>
    <div class="flex justify-end">
      <SearchForm/>
    </div>
    <MovieList
      v-for="movieData in movies"
      :key="movieData.genre"
      :movieList="movieData.data"
      :genre="movieData.genre"
    />
  </div>
</template>

<script>
import MovieList from '@/components/MovieList.vue'
import SearchForm from '@/components/SearchForm.vue'

export default {
  name: 'MovieView',
  components: {
    MovieList,
    SearchForm,
  },
  computed: {
    movies() {
      return this.$store.state.movies.movies
    }
  },
  created() {
    this.$store.dispatch('clearMovies')
    this.$store.dispatch('fetchMovies')
  },
  mounted() {
  }
}
</script>

<style>
.active {
  color: #42b983;
}

p {
  color: white;
}
</style>