<template>
  <div>
    <p>영화 상세 정보</p>
    {{ $route.params.moviePk }}
  </div>
</template>

<script>
export default {
  name: 'DetailView',
  methods: {
    // this.$route.params.moviePk => 영화 pk
  }
}
</script>

<style>

</style>