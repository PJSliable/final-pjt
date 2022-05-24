<template>
  <div class="flex justify-center items-center mb-10" style="margin-top: 100px">
    <div class="flex w-full justify-center">
      <div class="flex flex-col border-2 border-black bg-white rounded-lg p-5">
        <p class="flex flex-col text-4xl font-bold p-10 pb-5">리뷰 수정하기</p>
        <ReviewForm
          v-if="isReview"
          :review="review"
          action="update"
        />
      </div>
    </div>
    
    <hr>
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
    ...mapActions(['fetchReview'])
  },
  created() {
    this.fetchReview(this.$route.params.reviewPk)
  },
}
</script>

<style scoped>

</style>