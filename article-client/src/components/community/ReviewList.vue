<template>
  <table class="w-full text-sm bg-yellow-300 text-center text-gray-500">
    <thead class="text-xs text-gray-800 uppercase bg-">
        <tr>
          <th scope="col" class="px-6 py-3 font-GowunDodum">
              평점
          </th>
          <th scope="col" class="px-6 py-3 font-GowunDodum">
              영화 제목
          </th>
          <th scope="col" class="px-6 py-3 font-GowunDodum">
              리뷰 제목
          </th>
          <th scope="col" class="px-6 py-3 font-GowunDodum">
              작성자
          </th>
        </tr>
    </thead>
    <tbody>
      <tr
        v-for="(review, index) in reviews"
        :key="index"
        class="bg-gray-50 hover:bg-yellow-100"
        @click=reviewClick(review.pk)
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
        </td>
        <td class="px-6 py-4 font-GowunDodum">
          {{ review.movie.title }}
        </td>
        <td class="px-6 py-4 font-GowunDodum">
          {{ review.title }}
        </td>
        <td class="px-6 py-4 font-GowunDodum">
          {{ review.user.nickname }}
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
    reviewClick(reviewPk) {
      return this.$router.push({ name: 'reviewDetail', params: { reviewPk }})
    }
  }
}
</script>

<style scoped>

</style>