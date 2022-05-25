<template>
  <div class="flex justify-center items-center mb-10" style="margin-top: 100px">
    <div class="flex w-full justify-center">
      <div class="flex flex-col border-2 border-black bg-white rounded-lg p-5">
        <p class="flex flex-col text-4xl font-bold p-10 pb-5 font-DoHyeon">리뷰 작성하기</p>
        <ReviewForm
          :review="review"
          action="create"
        />
      </div>
    </div>

    <hr>
  </div>
</template>

<script>
import ReviewForm from '@/components/community/ReviewForm.vue'

export default {
  name: 'ReviewCreateView',
  components: {
    ReviewForm,
  },
  data() {
    return {
      review: {
        pk: null,
        rate: 0,
        title: '',
        content: '',
        moviePk: 0,
      }
    }
  },
}
</script>

<style scoped>

</style>