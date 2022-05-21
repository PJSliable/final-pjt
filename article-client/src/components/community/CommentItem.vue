<template>
  <div>
    <p>{{ comment }}</p>
  </div>
</template>

<script>
export default {
  name: 'CommentItem',
  props: {
    comment: {
      type: Object
    }
  }
}
</script>

<style scoped>

</style>