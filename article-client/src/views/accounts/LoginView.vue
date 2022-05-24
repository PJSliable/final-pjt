<template>
  <div class="flex justify-center top-1/2 items-center" style="margin-top: 100px">
    <div class="border-2 border-black bg-white rounded-lg p-5">
      <p class="font-Jua p-5 text-3xl">Login</p>

      <account-error-list v-if="authError"></account-error-list>

      <form @submit.prevent="login(credentials)" class="mt-5">
        <div class="flex flex-col justify-between gap-3">
          <p class="self-start font-Jua">아이디</p>
          <input class="border-2 border-slate-900 text-center px-1 font-Jua" type="text" name="username" v-model="credentials.username" required>
        </div>
        <br>
        <div class="flex flex-col justify-between gap-3">
          <p class="self-start font-Jua">비밀번호</p>
          <input class="border-2 border-slate-900" type="password" name="password" v-model="credentials.password" required>
        </div>
        <br>
        <button class="px-10 py-1 font-Jua bg-orange-400">로그인</button>
      </form>
    </div>
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