<template>
  <div>
    <p @click="getDetail" :data-movie-pk=movie.pk >카드</p>
  </div>
</template>

<script>
export default {
  name: 'MovieCard',
  props: {
    movie: {
      type: Object,
      required: true
    }
  },
  methods: {
    getDetail(event) {
      const moviePk = event.target.dataset.moviePk
      this.$router.push({ name: 'detail', params: { moviePk: moviePk } })
    },
  }
}
</script>

<style scoped>

</style>