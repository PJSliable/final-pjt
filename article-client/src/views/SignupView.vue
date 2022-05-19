<template>
  <div>
    <p>Signup!</p>
    <form @submit.prevent="onSubmit">
      <div class="flex flex-col">
        <div class="flex justify-between mb-5">
          <div class="flex flex-col">
            <p>ID</p><input type="text" name="username" v-model="signupInfo.username">
          </div>
          <div class="flex flex-col">
            <p>nickname</p><input type="text" name="nickname" v-model="signupInfo.nickname">
          </div>
        </div>
        <p>email</p><input type="email" name="email" v-model="signupInfo.email">
        <p>password1</p><input type="password" name="password1" v-model="signupInfo.password1">
        <p>password2</p><input type="password" name="password2" v-model="signupInfo.password2">
        <button>회원가입</button>
      </div>
    </form>
  </div>
</template>

<script>
import { signup } from '@/api/index.js'

export default {
  name: 'SignupView',
  data() {
    return {
      signupInfo: {
        username: '',
        nickname: '',
        password1: '',
        password2: '',
        email: '',
      },
    }
  },
  methods: {
    async onSubmit() {
      try {
        await signup(this.signupInfo)
        this.$router.push('/login')
      } catch(err) {
        alert(`문제가 발생했씁니다. ${err} 관리자에게 문의해주세요.`)
      }
    },
  },
}
</script>

<style scoped>

</style>