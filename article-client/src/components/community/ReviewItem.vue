<template>
  <tr>
    <td>
      {{ review.user.username }}
    </td>
    <td>
      <router-link 
        :to="{ name: 'reviewDetail', params: {reviewPk: review.pk} }">
        {{ review.title }}
      </router-link>
    </td>
    <td>
    ({{ commentCount }}) | {{ likeCount }}
    </td>
  </tr>
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