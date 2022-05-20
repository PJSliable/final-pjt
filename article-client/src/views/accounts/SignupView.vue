<template>
  <div>
    <p>Signup!</p>

    <account-error-list v-if="authError"></account-error-list>

    <form @submit.prevent="signup(credentials)">
      <div class="flex flex-col">
        <div class="flex justify-between mb-5">
          <div class="flex flex-col">
            <p>ID</p><input type="text" name="username" v-model="credentials.username">
          </div>
          <div class="flex flex-col">
            <p>nickname</p><input type="text" name="nickname" v-model="credentials.nickname">
          </div>
        </div>
        <p>email</p><input type="email" name="email" v-model="credentials.email">
        <p>password1</p><input type="password" name="password1" v-model="credentials.password1">
        <p>password2</p><input type="password" name="password2" v-model="credentials.password2">
        <button>회원가입</button>
      </div>
    </form>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import AccountErrorList from '@/components/AccountErrorList.vue'

export default {
  name: 'SignupView',
  components: {
    AccountErrorList,
  },
  data() {
    return {
      credentials: {
        username: '',
        nickname: '',
        email: '',
        password1: '',
        password2: '',
      }
    }
  },
  computed: {
    ...mapGetters(['authError'])
  },
  methods: {
    ...mapActions(['signup'])
  },
}
</script>

<style scoped>

</style>