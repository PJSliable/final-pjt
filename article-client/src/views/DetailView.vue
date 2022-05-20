<template>
  <div>
    <div>
    <p>영화 상세 정보</p>
    <p>{{ movie }}</p>
    <img :src="imageUrl" alt="">
    </div>
    <div>
      <p> 댓글 목록 </p>
      <div>
        <p>댓글작성폼</p>
      </div>
      <div>
        <p>댓글 목록</p>
        <p>{{ movie.user }}</p>
        <p>{{ movie.reviews }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: 'DetailView',
  computed: {
    movie() {
      return this.$store.state.movies.movieDetail
    },
    imageUrl() {
      return this.$store.state.movies.imageBaseUrl + this.movie.backdrop_path
    },
  },
  methods: {
    ...mapActions(['fetchDetail'])
  },
  created() {
    const payload = { moviePk: this.$route.params.moviePk }
    this.fetchDetail(payload)
  }
}
</script>

<style scoped>

</style>