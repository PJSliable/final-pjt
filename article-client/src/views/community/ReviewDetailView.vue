<template>
  <div class="flex flex-col items-center mt-10">
    <div class="p-1 md:p-3 flex flex-col justify-center items-center rounded-lg bg-white w-4/5 md:w-2/3">
      <div class="flex flex-col w-full px-1 md:px-5 lg:px-10">
        <div class="flex justify-center ">
          <p class="flex text-2xl font-bold p-3 md:text-4xl font-DoHyeon"><span class="users">{{nickname}}</span>님의 평가</p>
          <!-- isAuthor가 false로 출력됨 -->
          <div v-if="isAuthor" class="flex items-center gap-5">
            <router-link :to="{ name: 'reviewEdit', params: { reviewPk } }">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="16"
                height="16"
                fill="currentColor"
                class="bi bi-pen"
                viewBox="0 0 16 16"
              >
                <path
                  d="m13.498.795.149-.149a1.207 1.207 0 1 1 1.707 1.708l-.149.148a1.5 1.5 0 0 1-.059 2.059L4.854 14.854a.5.5 0 0 1-.233.131l-4 1a.5.5 0 0 1-.606-.606l1-4a.5.5 0 0 1 .131-.232l9.642-9.642a.5.5 0 0 0-.642.056L6.854 4.854a.5.5 0 1 1-.708-.708L9.44.854A1.5 1.5 0 0 1 11.5.796a1.5 1.5 0 0 1 1.998-.001zm-.644.766a.5.5 0 0 0-.707 0L1.95 11.756l-.764 3.057 3.057-.764L14.44 3.854a.5.5 0 0 0 0-.708l-1.585-1.585z"
                />
              </svg>
            </router-link>
            
            <button @click="deleteReview(reviewPk)">
              <svg
              xmlns="http://www.w3.org/2000/svg"
              width="16"
              height="16"
              fill="currentColor"
              class="bi bi-trash"
              viewBox="0 0 16 16"
            >
              <path
                d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"
              />
              <path
                fill-rule="evenodd"
                d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"
              />
            </svg>
            </button>
          </div>
        </div>
        <div class="container">
          <div class="flex w-full">
            <div class="w-1/2 my-5 flex justify-start md:justify-center">
              <div class="shadow-lg shadow-slate-900 rounded-lg h-max w-full sm:w-4/5 md:w-3/5 bg-white flex flex-col justify-between relative">
                <div @click="getDetail" class="cardImg border-2 border-b-black">
                  <img :src="imageUrl" alt="movie image" class="rounded-t-md" :data-movie-pk="moviePk" style="width:100%; height: 246px;">
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
            <div class="flex w-1/2 flex-col justify-between p-5 sm:py-10">
              <div class="self-start hidden sm:flex flex-col gap-3">
                <star-rating class=""
                      :increment="0.5"
                      :star-size="44"
                      :rating="review.rate"
                      :glow="2"
                      :show-rating="false"
                      :read-only="true"
                      color="#ff0000"
                    >
                </star-rating>
              </div>
              <div class="self-start flex flex-col gap-3 sm:hidden">
                <star-rating
                      :increment="0.5"
                      :star-size="25"
                      :rating="review.rate"
                      :glow="2"
                      :show-rating="false"
                      :read-only="true"
                      color="#ff0000"
                    >
                </star-rating>
              </div>

              <div class="self-start flex flex-col gap-5">
                <p class="font-bold text-l sm:text-xl md:text-2xl font-DoHyeon lg:text-4xl">{{ review.title }}</p>
                <span class="font-GowunDodum">{{ createdAt1 }}  {{ createdAt2 }}</span> 
                <p class="font-GowunDodum">{{ review.content }}</p>  
              </div>
              <div class="flex gap-3">
                <button @click="clickLike(reviewPk)">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-red-500" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd" d="M3.172 5.172a4 4 0 015.656 0L10 6.343l1.172-1.171a4 4 0 115.656 5.656L10 17.657l-6.828-6.829a4 4 0 010-5.656z" clip-rule="evenodd" />
                  </svg>
                </button>
                <p class="font-GowunDodum"><span class="users">{{ likeCount }}명</span><span class="hidden sm:inline">이 좋아합니다!</span></p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <CommentList
        :comments="review.comments"
      />
    </div>
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
      reviewPk: this.$route.params.reviewPk,
    }
  },
  computed: {
    ...mapGetters(['isAuthor', 'review', 'currentUser']),
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
      return this.$store.state.movies?.imageBaseUrl + this.review.movie?.poster_path
    },
    nickname() {
      return this.review.user?.nickname
    },
    createdAt1() {
      return this.review.created_at?.substr(0,10)
    },
    createdAt2() {
      return  this.review.created_at?.substr(11,8)
    },
  },
  methods: {
    ...mapActions(['fetchReview', 'likeReview', 'deleteReview']),
    getDetail(event) {
      const moviePk = event.target.dataset.moviePk
      this.$router.push({ name: 'detail', params: { moviePk: moviePk } })
    },
    clickLike() {
      this.likeReview(this.$route.params.reviewPk)
    }
  },
  created() {
    this.fetchReview(this.$route.params.reviewPk)
  },
}
</script>

<style scoped>
.users {
  color: black;
  opacity: 0.7;
}

.users:hover {
  cursor: pointer;
  color: red;
  opacity: 0.8;
}

.cardImg img {
  -webkit-transition: .3s ease-in-out;
  transition: .3s ease-in-out;
}

.cardImg img:hover {
  cursor: pointer;
  opacity: 0.7;
}
</style>