<template>
  <div class="flex flex-col w-full mt-10 pt-5 px-1 md:px-5 lg:px-10">
    <p class="flex text-2xl font-bold p-3 md:text-4xl font-DoHyeon justify-center">댓글 목록</p>

    <CommentForm class="mt-5"/>
    <table class="w-full text-sm bg-yellow-300 text-center text-gray-500 rounded-lg mt-10">
      <thead class="text-xs text-gray-800 uppercase">
        <tr>
          <th scope="col" class="px-6 py-3 font-GowunDodum">
            작성자
          </th >
          <th scope="col" class="px-6 py-3 font-GowunDodum">
            내용
          </th>
          <th scope="col" class="px-6 py-3 font-GowunDodum">
            작성일시
          </th>
          <th scope="col" class="py-3 font-GowunDodum">
          </th>
        </tr>
      </thead>
      <tbody>
        <CommentItem
          v-for="comment in comments"
          :key="comment.pk"
          :comment="comment"
        />
      </tbody>
    </table>
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