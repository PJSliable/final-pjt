<template>
  <div>
    <div>
      <router-link :to="{ name: 'movies' }">Total</router-link> |
      <router-link :to="{ name: 'mine' }">Mine</router-link> |
      <router-link :to="{ name: 'random' }">Random</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieView',
}
</script>

<style scoped>

</style>