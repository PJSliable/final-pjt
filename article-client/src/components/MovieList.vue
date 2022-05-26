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
    <div class="hidden lg:inline carousel-inner relative w-full overflow-hidden">
      <carousel
        class="flex mx-40"
        :items="6"
        :nav="false"
      >
      <button slot="prev" class="carousel-control-prev absolute z-10 top-0 bottom-0 flex items-center justify-center p-0 text-center border-0 hover:outline-none hover:no-underline focus:outline-none focus:no-underline left-0">
      <span class="carousel-control-prev-icon inline-block bg-no-repeat" aria-hidden="true"></span>
      </button>
        <MovieCard
          v-for="(movie, index) in movieList"
          :key="index"
          :movie="movie"
          :isLiked="false"
          class="mb-12"
        />
      <button slot="next" class="carousel-control-next absolute top-0 bottom-0 flex items-center justify-center p-0 text-center border-0 right-0">
        <span class="carousel-control-next-icon inline-block bg-no-repeat" aria-hidden="true"></span>
      </button>
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
.carousel-control-prev-icon {
 background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='%23000000' viewBox='0 0 8 8'%3E%3Cpath d='M5.25 0l-4 4 4 4 1.5-1.5-2.5-2.5 2.5-2.5-1.5-1.5z'/%3E%3C/svg%3E") !important;
}

.carousel-control-next-icon {
  background-image: url("data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='%23000000' viewBox='0 0 8 8'%3E%3Cpath d='M2.75 0l-1.5 1.5 2.5 2.5-2.5 2.5 1.5 1.5 4-4-4-4z'/%3E%3C/svg%3E") !important;
}
</style>