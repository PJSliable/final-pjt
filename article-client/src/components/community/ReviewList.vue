<template>
  <div class="flex justify-center">
    <table>
      <tbody>
        <tr class="odd:bg-red-600 even:bg-slate-100">
          <td>작성자</td>
          <td>제목</td>
          <td>댓글 수 / 좋아요 수</td>
        <tr/>
        <ReviewItem
          v-for="review in reviews"
          :key="review.pk"
          :review="review"
        />
    </tbody>
  </table>
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