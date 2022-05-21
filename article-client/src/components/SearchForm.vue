<template>
  <form @submit.prevent>
    <input
      type="text"
      class="border border-slate-500 rounded-sm w-full p-2"
      placeholder="검색하장"
      @input="onSearchDebounce"
      >
  </form>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'SearchForm',
  methods: {
    onSearchDebounce: _.debounce(function(event) {
      const userInput = event.target.value
      this.$store.dispatch('fetchSearchMovies', userInput)
    }, 400),
  },
}
</script>

<style scoped>

</style>