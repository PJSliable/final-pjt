<template>
  <div>
    <p>모든 카드 보여주기</p>
    <MovieCard/>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard.vue'


export default {
  name: 'MovieList',
  components: {
    MovieCard,
  },
}
</script>

<style scoped>
.active {
  color: #42b983;
}
</style>