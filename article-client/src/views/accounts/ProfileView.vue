<template>
  <div>
    <div>
      <p class="text-4xl"><span class="font-bold">{{ profile.username }}</span>님의 프로필!!</p>
    </div>
    <MyMovieList/>
    <MyReviewList :profile="profile"/>

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
