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
      <div class="flex flex-col items-center">
        <p class="ml-10 mt-8 font-semibold text-3xl md:text-4xl self-start font-DoHyeon">{{ username }}님 맞춤 추천 영화</p>
        <div class="w-full h-full grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 place-content-center">
          <MovieCard
            v-for="(movie, index) in recommendMovies[0]"
            :key="index"
            :movie="movie"
            :isLiked="false"
            class="mb-12"
          />
        </div>
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
import MovieCard from '@/components/MovieCard.vue'
import SearchForm from '@/components/SearchForm.vue'
import SearchMovieList from '@/components/SearchMovieList.vue'
import { mapGetters } from 'vuex'

export default {
  name: 'MovieView',
  components: {
    MovieList,
    MovieCard,
    SearchForm,
    SearchMovieList,
  },
  computed: {
    ...mapGetters(['currentUser']),
    recommendMovies() {
      return this.$store.state.movies.recommendMovies
    },
    movies() {
      return this.$store.state.movies.movies
    },
    isObjEmpty() {
      return Object.keys(this.$store.state.movies.searchMovies).length
    },
    username() {
      return this.currentUser.username
    }
  },
  created() {
    this.$store.dispatch('clearMovies')
    this.$store.dispatch('fetchMovies')
    this.$store.dispatch('fetchRecommedMovies')
  },
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