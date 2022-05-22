<template>
  <div>
      {{ profile.reviews }}
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
    name: 'MyReviewList',
    computed: {
        ...mapGetters(['profile']),
    },
}
</script>

<style scoped>

</style>