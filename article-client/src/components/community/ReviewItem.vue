<template>
  <div>
    {{ review.user.username }} : 

    <router-link 
      :to="{ name: 'reviewDetail', params: {reviewPk: review.pk} }">
      {{ review.title }}
    </router-link>

    ({{ commentCount }}) | +{{ likeCount }}
  </div>
</template>

<script>
export default {
  name: 'ReviewItem',
  props: {
    review: {
      type: Object,
      required: true,
    }
  },
  computed: {
    commentCount() {
      return this.review.comments?.length
    },
    likeCount() {
      return this.review.like_users?.length
    }
  },
}
</script>

<style scoped>

</style>