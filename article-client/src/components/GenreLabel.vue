<template>
  <div class="mt-1 px-2 rounded-lg shadow-lg border-2 border-slate-500">
    <p class="text-lg">{{ genreName }}</p>
  </div>
</template>

<script>
export default {
  name: 'GenreLabel',
  props: {
    genre: {
      type: Number,
      required: true,
    }
  },
  computed: {
    genreName() {
      return this.$store.state.movies.genres[this.genre]
    }
  }
}
</script>

<style scoped>

</style>