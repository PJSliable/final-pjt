<template>
  <form @submit.prevent="onSubmit">
    <p>{{this.$route.params.moviePk}}</p>
    <star-rating class="col-3"
      :show-rating="false"
      :increment="1"
      :glow="2"
      :clearable=true
      :star-size="40"
      v-model="newReview.rate"  
    >
    </star-rating>
    <div>
      <label for="title">title: </label>
      <input v-model="newReview.title" class="border" type="text" id="title" />
    </div>
    <div>
      <label for="content">contnet: </label>
      <textarea v-model="newReview.content" type="text" id="content"></textarea>
    </div>
    <div>
    </div>
    <button>{{ action }}</button>
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
p {
  font-size: 100px;
}
</style>