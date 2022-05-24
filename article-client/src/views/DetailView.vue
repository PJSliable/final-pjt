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
            <div>
              <p class="font-bold my-3 text-xl md:text-3xl lg:text-4xl">{{ movie.title }}</p>
            </div>

            <hr>
            <div class="my-3 text-2xl">
              <p>평점 : {{ movie.vote_average }},  개봉일 : {{ movie.release_date }},  장르 : {{ movie.genre_ids }}</p>
            </div>
            <div>
              <p class="my-3 text-2xl">줄거리</p>
              <p class="text-xl">{{ movie.overview }}</p>
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
      <div>
        <p class="mb-3">리뷰 목록</p>
        <ReviewList
          :reviews="movie.reviews"
        />
      </div>
    </div>
  </div>
</template>

<script>
import ReviewList from '@/components/community/ReviewList.vue'
import { mapActions } from 'vuex'

export default {
  name: 'DetailView',
  components: {
    ReviewList
  },
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
    }
  },
  methods: {
    ...mapActions(['fetchDetail'])
  },
  created() {
    const payload = { moviePk: this.$route.params.moviePk }
    this.fetchDetail(payload)
  }
}
</script>

<style scoped>


</style>