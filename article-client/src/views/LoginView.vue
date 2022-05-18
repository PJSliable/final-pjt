<template>
  <div>
    <p>Login!</p>
    <form @submit.prevent="onSubmit">
      <p>ID</p><input type="text" name="username" v-model="loginInfo.username">
      <p>password</p><input type="password" name="password" v-model="loginInfo.password">
      <button>LogIn</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data() {
    return {
      loginInfo: {
        username: '',
        password: '',
      },
    }
  },
  methods: {
    onSubmit() {},
  },
}
</script>

<style scoped>

</style>