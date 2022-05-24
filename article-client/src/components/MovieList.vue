<template>
  <div class="flex flex-col items-center">
    <p class="ml-10 mt-8 font-semibold text-3xl md:text-4xl self-start font-DoHyeon">{{ genreName }} 영화</p>
    <div class="w-full h-full grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 place-content-center">
      <MovieCard
        v-for="(movie, index) in movieList"
        :key="index"
        :movie="movie"
        :isLiked="false"
        class="mb-12"
      />
    </div>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard.vue'
import { mapGetters } from 'vuex'

export default {
  name: 'MovieList',
  components: {
    MovieCard,
  },
  props: {
    movieList:{
      type: Array,
      required: true,
    },
    genre: {
      type: Number,
      required: true,
    },
  },
  computed: {
    ...mapGetters(['genres']),
    genreName() {
      return this.genres[this.genre]
    }
  }
}
</script>

<style scoped>

</style>