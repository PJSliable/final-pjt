<template>
  <div>
    <p>{{ reviewPk }}번째 게시글</p>
    <router-link :to="{ name: 'detail', params: { moviePk } }" > 영화정보 바로가기</router-link>
    {{ review.movie }}
    <!-- 작성자 수정 삭제 button -->
    <div v-if="isAuthor">
      <router-link :to="{ name: 'reviewEdit', params: { reviewPk } }">
        <button>Edit</button>
      </router-link>
      |
      <button @click="deleteReview(reviewPk)">Delete</button>
    </div>
    <CommentList/>
  </div>
</template>

<script>
import CommentList from '@/components/community/CommentList.vue'
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'ReviewDetailView',
  components: {
    CommentList
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
      return this.$store.getters.review.movie
    },
  },
  methods: {
    ...mapActions(['fetchReview', 'likeReview', 'deleteReview'])
  },
  created() {
    this.fetchReview(this.reviewPk)
  },

}
</script>

<style scoped>

</style>