<template>
  <form @submit.prevent="onSubmit">
    <div class="w-full flex flex-col items-center gap-3 p-5">
      <star-rating class="pb-5"
        :show-rating="false"
        :increment="0.5"
        :glow="2"
        :clearable=true
        :star-size="40"
        v-model="newReview.rate"
      >
      </star-rating>
      <div class="w-full flex flex-col gap-3">
        <label class="self-start" for="title">리뷰 제목</label>
        <input v-model="newReview.title" class="border-2 border-slate-900 text-center px-1 font-Jua" type="text" id="title" />
      </div>
      <div class="w-full flex flex-col gap-3">
        <label class="self-start" for="content">내용 </label>
        <textarea v-model="newReview.content" type="text" id="content" class="border-2 border-slate-900 text-center px-1 font-Jua"></textarea>
      </div>
    </div>
    <div>
    </div>
    <button class="px-10 py-1 bg-orange-400">
      <span v-if="action==='create'">작성하기</span>
      <span v-else>수정하기</span>
    </button>
  </form>
</template>

<script>
import { mapActions } from 'vuex'
import StarRating from 'vue-star-rating'

export default {
  name: 'ReviewForm',
  components: {
    StarRating
  },
  props: {
    review: Object,
    action: String,
  },
  data() {
    return {
      newReview: {
        title: this.review.title,
        content: this.review.content,
        rate: this.review.rate,
      },
    }
  },
  methods: {
    ...mapActions(['createReview', 'updateReview']),
    onSubmit() {
      if (this.action === 'create') {
        const payload = {
          moviePk: this.$route.params.moviePk,
          ...this.newReview
        }
        this.createReview(payload)
      } else if (this.action === 'update') {
        const payload = {
          pk: this.review.pk,
          ...this.newReview
        }
        this.updateReview(payload)
      }
    }
  }
}
</script>

<style scoped>

</style>