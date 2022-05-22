<template>
  <div>
    <p>community</p>
    <div>
      <p>전체 리뷰 목록</p>
      <ReviewList
        :reviews="reviews"
      />
    </div>
  </div>
</template>

<script>
import ReviewList from '@/components/community/ReviewList.vue'
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommunityView',
  components: {
    ReviewList,
  },
  methods: {
    ...mapActions(['fetchReviews'])
  },
  computed: {
    ...mapGetters(['reviews'])
  },
  created() {
    this.fetchReviews()
  },
}
</script>

<style scoped>

</style>