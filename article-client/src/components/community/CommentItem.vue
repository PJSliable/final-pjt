<template>
  <div>
    <p>{{ comment }}</p>

    <form @submit.prevent="onSubmit" class="">
      <button class="border-2">delete</button>
    </form>


  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'CommentItem',
  props: {
    comment: {
      type: Object
    }
  },
  methods: {
    ...mapActions(['deleteComment']),
    onSubmit() {
      this.deleteComment({ commentPk:this.comment.pk , reviewPk:this.$route.params.reviewPk })
    }
  }
}
</script>

<style scoped>

</style>