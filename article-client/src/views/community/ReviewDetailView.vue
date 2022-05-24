<template>
  <div>
    <div class="w-full">
      <div class="rounded-lg bg-white w-2/3 md:w-1/2">
      <p>{{ review.username }} 님의 평가!</p>
      <div>
        <p>평가하신 영화: {{ review.movie.title }}</p>
      </div>
      <div class="flex">
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
      
      </div>
    </div>
    <p>{{ reviewPk }}번째 게시글</p>
    <router-link :to="{ name: 'detail', params: { moviePk: `${moviePk}` } }"> 영화정보 바로가기</router-link>
    {{ review.movie }}
    <div>
      <p>{{ review.rate }}</p>
      <p>{{ review.title }}</p>
      <p>{{ review.content }}</p>
    </div>
    <!-- 작성자 수정 삭제 button -->
    <div v-if="isAuthor">
      <router-link :to="{ name: 'reviewEdit', params: { reviewPk } }">
        <button>Edit</button>
      </router-link>
      |
      <button @click="deleteReview(reviewPk)">Delete</button>
    </div>

    <div>
      Likeit:
      <button class="border border-black"
        @click="likeReview(reviewPk)"
      >조아여</button>
    </div>
    <p>{{ likeCount }}</p>
    
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
      return this.review.movie
    },
  },
  methods: {
    ...mapActions(['fetchReview', 'likeReview', 'deleteReview'])
  },
  created() {
    this.fetchReview(this.$route.params.reviewPk)
  },

}
</script>

<style scoped>

</style>