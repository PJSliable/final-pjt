<template>
  <form @submit.prevent="onSubmit" class="items-center">
    <label for="comment" class="font-GowunDodum"></label>
    <input
      type="text"
      id="comment"
      v-model="content" required
      class="border-2 border-slate-900 text-center px-1 font-GowunDodum rounded-md"
    >
    <button class="createBtn px-3 py-1 bg-lime-300 m-2 border-t-2 border-lime-300 rounded-lg font-Jua">작성</button>
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
.font-sans {
  font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
}

.createBtn:hover {
  opacity: 0.9;
  transform: scale(1.03);
}
</style>