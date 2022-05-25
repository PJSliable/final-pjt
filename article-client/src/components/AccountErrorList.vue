<template>
  <div>
    <div v-for="(errors, field) in authError" :key="field">
        <div v-for="(error, idx) in errors" :key="idx">
            <div v-if="field==='username'">
              <div v-if="error==='A user with that username already exists.'">
                <p>이미 사용중인 아이디입니다.</p>
              </div>
              <div v-if="error==='This field may not be blank.'">
                <p>아이디를 입력해주세요.</p>
              </div>
            </div>
            <div v-if="field==='email' && error==='A user is already registered with this e-mail address.'">
              <p>이미 사용중인 이메일입니다.</p>
            </div>
            <div v-if="field==='password1'">
              <div v-if="error==='This password is too short. It must contain at least 8 characters.'">
                <p>비밀번호가 너무 짧습니다.</p>
                <p>8글자 이상 입력해주세요.</p>
              </div>
              <div v-if="error==='This field may not be blank.'">
                <p>비밀번호를 입력해주세요.</p>
              </div>
            </div>
            <div v-if="field==='password'">
              <div v-if="error==='This field may not be blank.'">
                <p>비밀번호 확인을 입력해주세요.</p>
              </div>
            </div>
            <div v-if="field==='nickname'">
              <div v-if="error==='This field may not be blank.'">
                <p>별명을 입력해주세요.</p>
              </div>
            </div>
            <div v-if="field==='non_field_errors'">
              <div v-if="error==='The password is too similar to the username.'">
                <p>비밀번호가 아이디와 유사합니다.</p>
              </div>
              <div :v-if="error===passwordE">
                <p>비밀번호 확인이 일치하지 않습니다.</p>
              </div>
            </div>
        </div>
    </div>
  </div>
</template>

<script>
  import { mapGetters } from 'vuex'
  
  export default {
    name: 'AccountErrorList',
    data() {
      return {
        passwordE: "The two password fields didn't match."
      }
    },
    computed: {
      ...mapGetters(['authError'])
    },
  }
</script>

<style scoped>
p {
  color: red;
  font-family: Jua;
}
</style>
