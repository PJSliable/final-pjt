<template>
  <div class="flex flex-col items-center mt-10">
    <div class="p-1 md:p-3 flex justify-center items-center rounded-lg bg-white w-4/5 md:w-2/3">
      <div class="flex flex-col w-full">
        <div class="flex justify-between px-10">
          <p>{{nickname}}님의 평가!</p>
          <div v-if="isAuthor">
            <router-link :to="{ name: 'reviewEdit', params: { reviewPk } }">
              <button>Edit</button>
            </router-link>
            |
            <button @click="deleteReview(reviewPk)">Delete</button>
          </div>
        </div>
      
      <div class="container">
        <div class="flex w-full">
          <div class="h-full w-1/2 flex justify-center my-5">
            <div class="shadow-lg shadow-slate-900 rounded-lg h-max w-4/5 bg-white flex flex-col justify-between relative">
              <div @click="getDetail" class="cardImg border-2 border-b-black">
                <img :src="imageUrl" alt="movie image" class="w-full rounded-t-md" :data-movie-pk="moviePk" style="width:100%; height: 246px;">
              </div>
              <div class="flex place-items-center" style="width: 100%; height: 100px;">
                <div class="flex-auto m-1">
                  <p class="text-xl font-bold font-GowunDodum text-center">{{ movieTitle }}</p>
                </div>
                <div class="flex m-2 flex-initial w-10">
                </div>
              </div>
            </div>
          </div>

          <div class="flex w-1/2 flex-col justify-center items-center">
            <div>
              <p>하사하신 평점 : </p>
              <star-rating
                    :increment="0.5"
                    :star-size="12"
                    :md-star-size="24"
                    :rating="review.rate"
                    :show-rating="false"
                    :read-only="true"
                    color="#ff0000"
                  >
              </star-rating>
            </div>
            <p>리뷰 제목: {{ review.title }}</p>
            <p>리뷰 내용: {{ review.content }}</p>
            <div>
              Likeit:
              <button class="border border-black"
                @click="likeReview(reviewPk)"
              >조아여</button>
            </div>
            <p>{{ likeCount }}</p>
            
          </div>
            </div>
          </div>
        </div>
      </div>
            <CommentList
              :comments="review.comments"
            />
  </div>

</template>

<script>
import CommentList from '@/components/community/CommentList.vue'
import { mapActions, mapGetters } from 'vuex'
import StarRating from 'vue-star-rating'

export default {
  name: 'ReviewDetailView',
  components: {
    CommentList,
    StarRating,
  },
  data() {
    return {
      reviewPk: this.$route.params.reviewPk
    }
  },
  computed: {
    ...mapGetters(['isAuthor', 'review']),
    likeCount() {
      return this.review.like_users?.length
    },
    moviePk() {
      return this.review.movie?.pk
    },
    movieTitle() {
      return this.review.movie?.title
    },
    imageUrl() {
      return this.$store.state.movies.imageBaseUrl + this.review.movie?.poster_path
    },
    nickname() {
      return this.review.user?.nickname
    }
  },
  methods: {
    ...mapActions(['fetchReview', 'likeReview', 'deleteReview']),
    getDetail(event) {
      const moviePk = event.target.dataset.moviePk
      this.$router.push({ name: 'detail', params: { moviePk: moviePk } })
    },
  },
  created() {
    this.fetchReview(this.$route.params.reviewPk)
  },

}
</script>

<style scoped>

</style>