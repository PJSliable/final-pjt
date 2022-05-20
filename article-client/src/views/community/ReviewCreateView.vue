<template>
  <div>
    <p>새로운 게시글 생성</p>
    {{ this.$route.params.moviePk }}
    {{ review }}
    <hr>
    <review-form
      :review="review"
      :moviePk="this.$route.params.moviePk"
      action="create"
    ></review-form>
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