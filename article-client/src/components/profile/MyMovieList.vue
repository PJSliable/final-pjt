<template>
  <div>
      <p>내 영화 카드</p>
      <div class="flex flex-wrap">
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