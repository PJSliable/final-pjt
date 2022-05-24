<template>
  <div>
      <div>
      <p>내 리뷰 목록</p>
      <div v-if="reviews">
        <ReviewList :reviews="reviews"/>
      </div>
    </div>
  </div>
</template>

<script>
import ReviewList from '@/components/community/ReviewList.vue'

export default {
    name: 'MyReviewList',
    components: {
        ReviewList,
    },
    props: {
        profile: {
            type: Object,
            required: true,
        }
    },
    computed: {
        reviews() {
            return this.profile.reviews
    }
  },
}
</script>

<style scoped>

</style>