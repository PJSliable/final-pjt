<template>
  <div>
    <div class="flex flex-col md:flex-row  md:justify-between">
      <div class="p-5 ml-5 mt-4 text-2xl md:text-4xl font-bold font-DoHyeon">
        <div v-if="isObjEmpty">
          <p>Search</p>
        </div>
        <div v-else>
          <p>{{ nickname }}님 반갑습니다.</p>
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
        <div class="flex self-start mt-5">
          <p class="ml-10 mx-5 font-semibold text-3xl md:text-4xl self-start font-DoHyeon">맞춤 추천 영화</p>
          <button @click.prevent="onRefresh" class=" self-middle w-7 h-30%">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path d="M449.9 39.96l-48.5 48.53C362.5 53.19 311.4 32 256 32C161.5 32 78.59 92.34 49.58 182.2c-5.438 16.81 3.797 34.88 20.61 40.28c16.97 5.5 34.86-3.812 40.3-20.59C130.9 138.5 189.4 96 256 96c37.96 0 73 14.18 100.2 37.8L311.1 178C295.1 194.8 306.8 223.4 330.4 224h146.9C487.7 223.7 496 215.3 496 204.9V59.04C496 34.99 466.9 22.95 449.9 39.96zM441.8 289.6c-16.94-5.438-34.88 3.812-40.3 20.59C381.1 373.5 322.6 416 256 416c-37.96 0-73-14.18-100.2-37.8L200 334C216.9 317.2 205.2 288.6 181.6 288H34.66C24.32 288.3 16 296.7 16 307.1v145.9c0 24.04 29.07 36.08 46.07 19.07l48.5-48.53C149.5 458.8 200.6 480 255.1 480c94.45 0 177.4-60.34 206.4-150.2C467.9 313 458.6 294.1 441.8 289.6z"/></svg>
          </button>
        </div>
        <div class="w-full h-full grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 place-content-center">
          <MovieCard
            v-for="(movie, index) in recommendMovies"
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
    ...mapGetters(['currentUser', 'recommendMovies']),
    movies() {
      return this.$store.state.movies.movies
    },
    isObjEmpty() {
      return Object.keys(this.$store.state.movies.searchMovies).length
    },
    username() {
      return this.currentUser.username
    },
    nickname() {
      return this.currentUser.nickname
    },
  },
  methods: {
    onRefresh() {
      return this.$store.dispatch('fetchRecommedMovies')
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