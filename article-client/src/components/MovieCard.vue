<template>
    <div class="my-3 w-1/4 p-5">
      <div>
        <div class="border border-2 border-black flex flex-col items-center justify-between my-3">
          <div @click="getDetail">
            <img :src="imageUrl" alt="movie image" class="w-auto" :data-movie-pk="movie.pk">
          </div>
          <div class="flex justify-between items-center">
            <div class="w-4/5 flex">
              <span class="movieTitle font-bold text-1/2 text-white">{{ movie.title }}</span>
            </div>
            <div class="text-center">
              <span class="font-bold text-1/2 text-white">{{ movie.vote_average }}</span>
            </div>
          </div>
        </div>
      </div>
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
  computed: {
    imageUrl() {
      return this.$store.state.movies.imageBaseUrl + this.movie.poster_path
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