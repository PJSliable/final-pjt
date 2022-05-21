<template>
  <form @submit.prevent="onSubmit" class="">
    <label for="comment">comment: </label>
    <input
      type="text"
      id="comment"
      v-model="content" required
      class="border"
    >
    <button class="border-2">댓글 작성 버튼</button>
  </form>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentForm',
  data() {
    return {
      content: ''
    }
  },
  computed: {
    ...mapGetters(['review']),
  },
  methods: {
    ...mapActions(['createComment']),
    onSubmit() {
      this.createComment({ reviewPk: this.review.pk, content: this.content, })
      this.content = ''
    }
  }
}
</script>

<style scoped>

</style>