<template>
  <div class="flex flex-col items-center w-full pt-10">
    <div>
      <span class="font-bold text-3xl md:text-4xl font-DoHyeon">{{ profile.nickname }}님의 프로필</span>
    </div>
    <MyMovieList/>
    <MyReviewList
      class="w-full md:w-2/3 mb-20"
      :profile="profile"
    />
  </div>
</template>

<script>
import MyMovieList from '@/components/profile/MyMovieList.vue'
import MyReviewList from '@/components/profile/MyReviewList.vue'
import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'ProfileView',
  components: {
    MyMovieList,
    MyReviewList,
  },
  computed: {
    ...mapGetters(['profile'])
  },
  methods: {
    ...mapActions(['fetchProfile'])
  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
  },
}
</script>

<style scoped>

</style>
