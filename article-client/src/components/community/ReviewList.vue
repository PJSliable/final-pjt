<template>
  <table class="w-full text-sm bg-green-400 text-left text-gray-500">
    <thead class="text-xs text-gray-800 uppercase bg-">
        <tr>
          <th scope="col" class="px-6 py-3">
              평점
          </th>
          <th scope="col" class="px-6 py-3">
              리뷰 제목
          </th>
          <th scope="col" class="px-6 py-3">
              작성자
          </th>
        </tr>
    </thead>
    <tbody>
      <tr
        v-for="(review, index) in reviews"
        :key="index"
        class="bg-lime-100 hover:bg-lime-200"
        @click=reviewClick(review.movie)
      >
        <td class="px-6 py-4">
          <star-rating
            :increment="0.5"
            :star-size="12"
            :md-star-size="24"
            :rating="review.rate"
            :show-rating="false"
            :read-only="true"
            color="#ff0000"
          >
          </star-rating>
        <td class="px-6 py-4">
          {{ review.title }}
        </td>
        <td class="px-6 py-4">
          {{ review.user.username }}
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import StarRating from 'vue-star-rating'

export default {
  name: 'ReviewList',
  components: {
    StarRating,
  },
  props: {
    reviews: {
      type: Array,
      required: true,
    },
  },
  methods: {
    reviewClick(moviePk) {
      return this.$router.push({ name: 'detail', params: { moviePk }})
    }
  }
}
</script>

<style scoped>

</style>