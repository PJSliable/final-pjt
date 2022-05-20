<template>
  <div>
    <p>리뷰 수정하기</p>
    <ReviewForm
      v-if="isReview"
      :review="review"
      action="update"
    />
  </div>
</template>

<script>
import ReviewForm from '@/components/community/ReviewForm.vue'
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'ReviewEditView',
  components: {
    ReviewForm,
  },
  computed: {
    ...mapGetters(['review', 'isReview'])
  },
  methods: {
    ...mapActions(['fetchRevie'])
  },
  created() {
    this.fetchReview(this.$route.params.reviewPk)
  },
}
</script>

<style scoped>

</style>