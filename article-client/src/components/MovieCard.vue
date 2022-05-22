<template>
    <div class="my-3 w-1/4 p-5">
      <div>
        <div class="border border-2 border-black flex flex-col my-3">
          <div @click="getDetail">
            <img :src="imageUrl" alt="movie image" class="w-auto" :data-movie-pk="movie.pk">
          </div>
          <div class="flex flex-col w-full">
            <div class="flex items-center justify-between">
              <form @submit.prevent="clickLike" :data-movie-pk="movie.pk">
                <button  class="border-2 border-black px-2" >
                  <span  v-if="likeState">시러용</span>
                  <span  v-else>조아용</span>
                </button>
              </form>
              <span class="font-bold text-1/2">{{ movie.vote_average }}</span>
            </div>
            <div>
              <span class="movieTitle font-bold text-1/2">{{ movie.title }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'MovieCard',
  props: {
    movie: {
      type: Object,
      required: true
    },
    isLiked: {
      type: Boolean,
      required: true,
    }
  },
  computed: {
    imageUrl() {
      return this.$store.state.movies.imageBaseUrl + this.movie.poster_path
    },
    likeState() {
      return this.isLiked
    } 
  },
  methods: {
    ...mapActions(['likeMovie']),
    getDetail(event) {
      const moviePk = event.target.dataset.moviePk
      this.$router.push({ name: 'detail', params: { moviePk: moviePk } })
    },
    clickLike(event) {
      const moviePk = event.target.dataset.moviePk
      this.likeMovie(moviePk)
    }
  }
}
</script>

<style scoped>

</style>