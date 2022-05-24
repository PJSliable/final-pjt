<template>
  <div>
    <!-- <div>
      <span class="text-4xl font-bold">{{ profile.nickname }}</span>
    </div> -->
    <MyMovieList/>
    <MyReviewList :profile="profile" class="w-2/3 justify-center"/>

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
