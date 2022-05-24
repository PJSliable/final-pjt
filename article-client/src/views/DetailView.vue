<template>
  <div class="relative">
    <div v-if="this.movie.backdrop_path" class="flex flex-col justify-center items-center">
      <img :src="bgImgUrl" alt="backgroundImg" class="absolute pointer-events-none top-0 z-0 opacity-20 blur-sm w-full">
      <div class="flex z-10 pt-3 flex justify-center items-center">
        <div class="grid border-2 grid-cols-3 flex w-4/5 md:w-2/3">
          <div class="w-full flex justify-center items-center">
            <img :src="ptImgUrl" alt="posterImg" class="w-full" style="width:100%; height: 100%;">
          </div>
          <div class="col-span-2 w-full p-3">
            <div class="flex">
              <p class="font-bold text-xl md:text-3xl lg:text-4xl">{{ movie.title }}</p>
            </div>

            <div>
              <p>줄거리</p>
              <p>{{ movie.overview }}</p>
            </div>

          </div>
        </div>
      </div>
      <hr>
      <div>
        <div>
          <router-link
            :to="{ name: 'reviewCreate', params: { moviePk: moviePk } }"
          >
          <button class="px-10 py-1 m-3 font-Jua bg-orange-400">리뷰작성하기</button>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'DetailView',
  data() {
    return {
      moviePk: this.$route.params.moviePk
    }
  },
  computed: {
    movie() {
      return this.$store.state.movies.movieDetail
    },
    bgImgUrl() {
      return this.$store.state.movies.imageBaseUrl + this.movie.backdrop_path
    },
    ptImgUrl() {
      return this.$store.state.movies.imageBaseUrl + this.movie.poster_path
    },
  },
  methods: {
    ...mapActions(['fetchDetail']),
    reviewClick(reviewPk) {
      return this.$router.push({ name: 'reviewDetail', params: { reviewPk }})
    }
  },
  created() {
    const payload = { moviePk: this.$route.params.moviePk }
    this.fetchDetail(payload)
  }
}
</script>

<style scoped>


</style>