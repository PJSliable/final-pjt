<template>
    <div class="h-full w-full flex justify-center my-5">
      <div class="shadow-lg shadow-slate-900 rounded-lg h-max w-4/5 bg-white flex flex-col justify-between relative">
        <div @click="getDetail" class="border-2 border-b-black">
          <img :src="imageUrl" alt="movie image" class="w-full rounded-t-md" :data-movie-pk="movie.pk" style="width:100%; height: 246px;">
        </div>
        <div class="flex flex-col justify-evenly" style="width: 100%; height: 100px;">
          <div class="flex justify-end mx-2">
            <form @submit.prevent="clickLike" :data-movie-pk="movie.pk" >
              <button  class="border-2 border-black px-2" >
                <span v-if="likestate">시러용</span>
                <span v-else>조아용</span>
              </button>
            </form>
          </div>
          <div class="" >
            <p class="font-bold text-sm">{{ movie.title }}</p>
          </div>
        </div>
        <div class="rounded-full p-2 font-bold text-white text-1/5 absolute left-1 top-1 bg-slate-700" style="width:40px; height:40px;">
          <span>{{ movie.vote_average }}</span>
        </div>
      </div>
    </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'MovieCard',
  data() {
    return {
      likeState: this.isLiked
    }
  },
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
    likestate() {
      return this.likeState
    },
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
      this.likeState = !this.likeState
    }
  }
}
</script>

<style scoped>

</style>