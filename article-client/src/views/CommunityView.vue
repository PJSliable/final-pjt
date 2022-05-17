<template>
  <div>
    <h1>community</h1>
    <ReviewList/>
  </div>
</template>

<script>
import ReviewList from '@/components/ReviewList.vue'

export default {
  name: 'CommunityView',
  components: {
    ReviewList,
  }
}
</script>

<style scoped>

</style>