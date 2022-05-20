<template>
  <div>
    <div>
    <p>영화 상세 정보</p>
    <p>{{ movie }}</p>
    <p>{{ moviePk }}</p>
    <img :src="imageUrl" alt="">
    </div>
    <div>
      <p> 리뷰 목록 </p>
      <div>
        <p>리뷰작성하기</p>
        <router-link
          :to="{ name: 'reviewCreate', params: { moviePk: moviePk } }"
        >Create</router-link>
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
  data() {
    return {
      moviePk: this.$route.params.moviePk
    }
  },
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