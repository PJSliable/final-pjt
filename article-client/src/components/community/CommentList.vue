<template>
  <div class="flex flex-col w-full mt-10 pt-5 px-1 md:px-5 lg:px-10">
    <p class="flex text-2xl font-bold p-3 md:text-4xl font-DoHyeon">리뷰 목록!</p>

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
.font-sans {
  font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
}
</style>