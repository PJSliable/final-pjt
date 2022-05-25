<template>
  <form @submit.prevent class="relative z-0 mx-7">
    <input
      type="text"
      class="border border-slate-500 rounded-lg w-full p-2 pl-16"
      placeholder="영화 제목을 검색하세요."
      @input="onSearchDebounce"
      >
    <div class="searchIcon align-center absolute top-1">
      <span class="align-middle border-r-2 border-slate-300 text-2xl pl-2 px-1">🔍</span>
    </div>
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
.searchIcon:hover {
  cursor: Default;
}
</style>