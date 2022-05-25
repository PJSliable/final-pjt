<template>
  <div class="flex flex-col">
    <p class="ml-10 mt-8 font-semibold text-3xl md:text-4xl self-start font-DoHyeon">{{ genreName }} 영화</p>
    <div class="sm:hidden">
      <carousel
        :items="2"
        :loop="false"
        :nav="false"
      >
        <MovieCard
          v-for="(movie, index) in movieList"
          :key="index"
          :movie="movie"
          :isLiked="false"
          class="mb-12"
        />
      </carousel>
    </div>
    <div class="hidden sm:inline md:hidden">
      <carousel
        :items="3"
        :loop="false"
        :nav="false"
      >
        <MovieCard
          v-for="(movie, index) in movieList"
          :key="index"
          :movie="movie"
          :isLiked="false"
          class="mb-12"
        />
      </carousel>
    </div>
    <div class="hidden md:inline lg:hidden">
      <carousel
        :items="4"
        :loop="false"
        :nav="false"
      >
        <MovieCard
          v-for="(movie, index) in movieList"
          :key="index"
          :movie="movie"
          :isLiked="false"
          class="mb-12"
        />
      </carousel>
    </div>
    <div class="hidden lg:inline">
      <carousel
        :items="6"
        :loop="false"
        :nav="false"
      >
        <MovieCard
          v-for="(movie, index) in movieList"
          :key="index"
          :movie="movie"
          :isLiked="false"
          class="mb-12"
        />
      </carousel>
    </div>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard.vue'
import { mapGetters } from 'vuex'
import carousel from 'vue-owl-carousel'

export default {
  name: 'MovieList',
  components: {
    MovieCard,
    carousel,
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