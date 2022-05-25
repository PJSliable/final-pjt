<template>
  <div class="relative">
    <div v-if="bgImgUrl" class="flex flex-col justify-center items-center mt-10">
      <img :src="bgImgUrl" alt="backgroundImg" class="hidden lg:inline absolute pointer-events-none top-0 z-0 opacity-30 blur-sm w-full">
      <div class="flex z-10 pt-3 flex justify-center items-center">
        <div class="grid shadow-slate-600 shadow-lg rounded-lg grid-cols-3 bg-white flex w-4/5 md:w-2/3">
          <div class="w-full flex justify-center items-center">
            <img :src="ptImgUrl" alt="posterImg" class="w-full rounded-l-lg" style="width:100%; height: 100%;">
          </div>

          <div class="col-span-2 w-full p-3">
            <div>
              <p class="font-bold my-3 text-xl md:text-3xl lg:text-4xl">{{ movie.title }}</p>
            </div>
            <div class="my-3 text-xl font-bold font-GowunDodum">
              <p>평점 : {{ movie.vote_average }},  개봉일 : {{ movie.release_date }}</p>
                <div class="flex justify-center gap-3">
                  <GenreLabel
                    v-for="(genre, index) in genres"
                    :key="index"
                    :genre="genre"
                  />
                </div>
              
            </div>
            <div class="flex flex-col p-3">
              <p class="self-start my-3 text-2xl font-bold font-GowunDodum">줄거리</p>
              <p class="text-left text-xl font-GowunDodum">{{ movie.overview }}</p>
            </div>
          </div>


          <div class="col-span-3">
            <div>
              <div class="p-10">
                <router-link
                  :to="{ name: 'reviewCreate', params: { moviePk: moviePk } }"
                >
                  <button class="px-10 py-1 m-3 font-Jua bg-orange-400 rounded-lg">리뷰 작성하러 가기</button>
                </router-link>
              </div>
            </div>
            <div v-if="isReviews">
              <hr>
              <p class="text-4xl py-10 font-semibold font-DoHyeon">리뷰 목록</p>
              <div class="w-full flex flex-wrap pb-10">
                <div
                  v-for="(review, index) in reviews"
                  :key="index"
                  class="text-black text-2xl text-Jua rounded-lg flex justify-center w-1/2"
                >
                  <td class="px-6 py-4">
                    <star-rating
                      :increment="0.5"
                      :star-size="35"
                      :glow="5"
                      :rating="review.rate"
                      :show-rating="false"
                      :read-only="true"
                      color="#ff0000"
                    >
                    </star-rating>
                  </td>
                  <td class="px-6 py-4 font-GowunDodum">
                    <p>{{ review.title }}</p>
                  </td>
                </div>
              </div>
            </div>
            <div v-else class="rounded-md bg-white">
              <p class="p-10 text-4xl font-semibold font-DoHyeon">아직 작성된 리뷰가 없습니다!</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    
  </div>
</template>

<script>
import GenreLabel from '@/components/GenreLabel.vue'
import { mapActions } from 'vuex'
import StarRating from 'vue-star-rating'

export default {
  name: 'DetailView',
  components: {
    GenreLabel,
    StarRating,
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
      return this.$store.state.movies.imageBaseUrl + this.$store.getters.backdropImg
    },
    ptImgUrl() {
      return this.$store.state.movies.imageBaseUrl + this.movie?.poster_path
    },
    reviews() {
      return this.$store.getters.movieDetail.reviews
    },
    isReviews() {
     return this.$store.getters.movieDetail.reviews?.length
    },
    genres() {
      return this.$store.getters.movieDetail.genre_ids
    }
  },
  methods: {
    ...mapActions(['fetchDetail']),
  },
  created() {
    const payload = { moviePk: this.$route.params.moviePk }
    this.fetchDetail(payload)
  }
}
</script>

<style scoped>
</style>