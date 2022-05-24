<template>
  <div>
    <p class="text-2xl font-bold p-10 md:text-4xl font-DoHyeon">내 리뷰 목록</p>
    <div v-if="reviews">
      <ReviewList :reviews="reviews"/>
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