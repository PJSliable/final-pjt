<template>
  <div>
    <p>내 영화 카드</p>
    <div class="w-full h-full grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 gap-4 place-content-center">
      <MovieCard
        v-for="movie in profile.my_movies"
        :key="movie.pk"
        :movie="movie"
        :isLiked="true"
      />
    </div>
  </div>
  
</template>

<script>
import MovieCard from '@/components/MovieCard.vue'
import { mapGetters } from 'vuex'

export default {
    name: 'MyMovieList',
    components: {
        MovieCard,
    },
    computed: {
        ...mapGetters(['profile']),
    },
}
</script>

<style scoped>

</style>