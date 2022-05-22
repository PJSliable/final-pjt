<template>
  <div>
      {{ profile.my_movies }}
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
    name: 'MyMovieList',
    computed: {
        ...mapGetters(['profile']),
    },
}
</script>

<style scoped>

</style>