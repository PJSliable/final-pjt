<template>
  <div class="h-screen">
    <p class="font-extrabold mt-5">Login</p>

    <account-error-list v-if="authError"></account-error-list>

    <form @submit.prevent="login(credentials)">
      <p>ID</p><input class="border-2 border-slate-900" type="text" name="username" v-model="credentials.username" required>
      <p>password</p><input class="border-2 border-slate-900" type="password" name="password" v-model="credentials.password" required>
      <button>Login</button>
    </form>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import AccountErrorList from '@/components/AccountErrorList.vue'

export default {
  name: 'LoginView',
  components: {
    AccountErrorList,
  },
  data() {
    return {
      credentials: {
        username: '',
        password: '',
      }
    }
  },
  computed: {
    ...mapGetters(['authError'])
  },
  methods: {
    ...mapActions(['login'])
  },
}
</script>

<style scoped>

</style>