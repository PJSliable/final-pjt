<template>
  <div>
    <h1>Logout</h1>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import Swal from 'sweetalert2'

export default {
  methods: {
    ...mapActions(['logout'])
  },
  computed: {
    ...mapGetters(['isLoggedIn'])
  },
  mounted() {
    if (this.isLoggedIn) {
      this.logout()
    } else {
      Swal.fire({
        icon: 'error',
        title: '비정상적 접근',
        text: '다시 시도해주세요.'
      })
      this.$router.back()
    }
  },
}
</script>

<style scoped>

</style>
