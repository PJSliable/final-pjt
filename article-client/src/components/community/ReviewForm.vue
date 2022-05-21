<template>
  <form @submit.prevent="onSubmit">
    <p>{{this.$route.params.moviePk}}</p>
    <div>
      <label for="title">title: </label>
      <input v-model="newReview.title" type="text" id="title" />
    </div>
    <div>
      <label for="content">contnet: </label>
      <textarea v-model="newReview.content" type="text" id="content"></textarea>
    </div>
    <div>
      <label for="rate">rate: </label>
      <input v-model.number="newReview.rate" min="0" max="5" id="rate">
    </div>
    <button>{{ action }}</button>
  </form>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'ReviewForm',
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
          movie: this.$route.params.moviePk,
          ...this.newReview
        }
        this.createReview(payload)
      } else if (this.action === 'update') {
        const payload = {
          pk: this.review.pk,
          movie: this.review.movie,
          ...this.newReview
        }
        const data = {
          review: payload,
          reviewPk: this.review.pk
        }
        this.updateReview(data)
      }
    }
  }
}
</script>

<style scoped>

</style>