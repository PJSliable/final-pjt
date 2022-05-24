<template>
<div class="flex justify-center top-1/2 items-center" style="margin-top: 100px">
    <div class="border-2 border-black bg-white rounded-lg p-5">
      <p class="font-Jua p-5 text-3xl">Sign up</p>

      <account-error-list v-if="authError"></account-error-list>

      <form @submit.prevent="signup(credentials)">
      <div class="flex flex-col justify-between gap-3">
        <div class="flex justify-between gap-3">
          <div class="flex flex-col">
            <p class="self-start font-Jua">아이디</p>
            <input class="border-2 border-slate-900 text-center px-1 font-Jua" type="text" name="username" v-model="credentials.username">
          </div>
          <div class="flex flex-col">
            <p class="self-start font-Jua">별명</p>
            <input class="border-2 border-slate-900 text-center px-1 font-Jua" type="text" name="nickname" v-model="credentials.nickname">
          </div>
        </div>
        <div class="flex flex-col">
          <p class="self-start font-Jua">이메일</p>
          <input class="border-2 border-slate-900 text-center px-1 font-Jua" type="email" name="email" v-model="credentials.email">
        </div>
        <div class="flex flex-col">
          <p class="self-start font-Jua">비밀번호</p>
          <input class="border-2 border-slate-900 text-center px-1" type="password" name="password1" v-model="credentials.password1">
        </div>
        <div class="flex flex-col">
          <p class="self-start font-Jua">비밀번호 확인</p>
          <input class="border-2 border-slate-900 text-center px-1" type="password" name="password2" v-model="credentials.password2"> 
        </div>
        <br>
        <button class="px-10 py-1 bg-orange-400 font-Jua">회원가입</button>
      </div>
    </form>
    </div>
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