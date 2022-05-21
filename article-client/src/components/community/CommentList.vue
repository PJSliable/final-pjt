<template>
  <div>
    <CommentForm/>
    <CommentItem
      v-for="comment in comments"
      :key="comment.pk"
      :comment="comment"
    />
  </div>
</template>

<script>
import CommentForm from '@/components/community/CommentForm.vue'
import CommentItem from '@/components/community/CommentItem.vue'

export default {
  name: 'CommentList',
  components: {
    CommentForm,
    CommentItem,
  },
  props: {
    comments: {
      type: Array,
    }
  }
}
</script>

<style scoped>

</style>