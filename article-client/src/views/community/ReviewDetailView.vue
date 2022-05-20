<template>
  <div>
    <p></p>
    <!-- 수정 삭제 button -->
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