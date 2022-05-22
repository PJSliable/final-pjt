<template>
  <div>
    <ReviewItem
      v-for="review in reviews"
      :key="review.pk"
      :review="review"
    />
  </div>
</template>

<script>
import ReviewItem from '@/components/community/ReviewItem.vue'

export default {
  name: 'ReviewList',
  components: {
    ReviewItem,
  },
  props: {
    reviews: {
      type: Array,
      required: true,
    },
  },
}
</script>

<style scoped>

</style>