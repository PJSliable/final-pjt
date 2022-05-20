<template>
  <div>
    <p>community</p>
    <ReviewList/>
  </div>
</template>

<script>
import ReviewList from '@/components/community/ReviewList.vue'

export default {
  name: 'CommunityView',
  components: {
    ReviewList,
  }
}
</script>

<style scoped>

</style>