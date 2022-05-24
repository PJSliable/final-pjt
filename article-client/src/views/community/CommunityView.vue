<template>
  <div>
    <p class="flex text-4xl font-bold p-10">댓글쓰쉴?</p>
    <div class="w-full flex justify-center">
      <div class="flex flex-col w-2/3 items-center">
        <p class="flex text-2xl font-bold p-10">전체 리뷰 목록</p>
        <ReviewList
          :reviews="reviews"
        />
      </div>
    </div>
  </div>
</template>

<script>
import ReviewList from '@/components/community/ReviewList.vue'
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommunityView',
  components: {
    ReviewList,
  },
  methods: {
    ...mapActions(['fetchReviews'])
  },
  computed: {
    ...mapGetters(['reviews'])
  },
  created() {
    this.fetchReviews()
  },
}
</script>

<style scoped>

</style>