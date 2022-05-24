<template>
    <div class="h-full w-full flex justify-center my-5">
      <div class="shadow-lg shadow-slate-900 rounded-lg h-max w-4/5 bg-white flex flex-col justify-between relative">
        <div @click="getDetail" class="cardImg border-2 border-b-black">
          <img :src="imageUrl" alt="movie image" class="w-full rounded-t-md" :data-movie-pk="movie.pk" style="width:100%; height: 246px;">
        </div>
        <div class="flex place-items-center" style="width: 100%; height: 100px;">
          <div class="flex-auto m-1">
            <p class="text-xl font-bold font-GowunDodum text-center">{{ movie.title }}</p>
          </div>
          <div class="flex m-2 flex-initial w-10">
            <form @submit.prevent="clickLike" :data-movie-pk="movie.pk" >
              <button class="px-2" >
                <span v-if="likestate">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-red-500" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M3.172 5.172a4 4 0 015.656 0L10 6.343l1.172-1.171a4 4 0 115.656 5.656L10 17.657l-6.828-6.829a4 4 0 010-5.656z" clip-rule="evenodd" />
                  </svg>
                </span>
                <span v-else>
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-red-500" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
                  </svg>
                </span>
              </button>
            </form>
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
.cardImg img {
  -webkit-transition: .3s ease-in-out;
  transition: .3s ease-in-out;
}

.cardImg img:hover {
  cursor: pointer;
  opacity: 0.5;
}
</style>