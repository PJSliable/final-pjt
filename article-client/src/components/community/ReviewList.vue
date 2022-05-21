<template>
  <div>
    <p>게시글 목록</p>
    <ul>
      <li v-for="review in reviews" :key="review.pk">
        {{ review.user.username }} : 

        <router-link 
          :to="{ name: 'reviewDetail', params: {reviewPk: review.pk} }">
          {{ review.title }}
        </router-link>

        ({{ review.comment_count }}) | +{{ review.like_count }}
      </li>
    </ul>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'ReviewList',
  computed: {
    ...mapGetters(['reviews'])
  },
  methods: {
    ...mapActions(['fetchReviews'])
  },
  created() {
    this.fetchReviews()
  },
}
</script>

<style scoped>

</style>