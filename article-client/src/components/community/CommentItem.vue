<template>
  <tr class="bg-gray-50">
    <td class="px-6 py-4 font-GowunDodum">
      <router-link :to="{ name: 'profile', params: { nickname: comment.user.nickname } }" class="font-GowunDodum">
        <span class="users">{{ comment.user.nickname }}</span>
      </router-link>
    </td>

    <td class="px-6 py-4 font-GowunDodum">
      <span v-if="!isEditing" class="font-GowunDodum">{{ payload.content }}</span>
      <span v-else>
        <input class="border-2 border-slate-900 text-center px-1 font-GowunDodum rounded-md" type="text" v-model="payload.content">
      </span>
    </td>

    <td class="px-6 py-4 font-GowunDodum">
      <span class="font-GowunDodum">
        {{ createdAt1 }}  {{ createdAt2 }}
      </span>
    </td>

    <td class="py-4 font-GowunDodum">
      <div v-if="currentUser.username === comment.user.username">
        <span v-if="isEditing" class="flex items-center justify-center gap-3">
          <button @click="updateC" class="font-GowunDodum ml-2">수정</button>
          <button @click="switchIsEditing" class="font-GowunDodum">취소</button>
        </span>
        
        <span v-else class="flex items-center justify-center gap-4">
          <button @click="switchIsEditing">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="16"
              height="16"
              fill="currentColor"
              class="bi bi-pen"
              viewBox="0 0 16 16"
            >
              <path
                d="m13.498.795.149-.149a1.207 1.207 0 1 1 1.707 1.708l-.149.148a1.5 1.5 0 0 1-.059 2.059L4.854 14.854a.5.5 0 0 1-.233.131l-4 1a.5.5 0 0 1-.606-.606l1-4a.5.5 0 0 1 .131-.232l9.642-9.642a.5.5 0 0 0-.642.056L6.854 4.854a.5.5 0 1 1-.708-.708L9.44.854A1.5 1.5 0 0 1 11.5.796a1.5 1.5 0 0 1 1.998-.001zm-.644.766a.5.5 0 0 0-.707 0L1.95 11.756l-.764 3.057 3.057-.764L14.44 3.854a.5.5 0 0 0 0-.708l-1.585-1.585z"
              />
            </svg>
          </button>
          <form @submit.prevent="deleteC">
            <button>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="16"
                height="16"
                fill="currentColor"
                class="bi bi-trash"
                viewBox="0 0 16 16"
              >
                <path
                  d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"
                />
                <path
                  fill-rule="evenodd"
                  d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"
                />
              </svg>
            </button>
          </form>
        </span>
      </div>
    </td>
  </tr>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentItem',
  props: {
    comment: {
      type: Object
    }
  },
  data() {
    return {
      isEditing: false,
      payload: {
        reviewPk: this.$route.params.reviewPk,
        commentPk: this.comment.pk,
        content: this.comment.content,
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
    nickname() {
      return this.currentUser?.nickname
    },
    createdAt1() {
      return this.comment.created_at?.substr(5,5)
    },
    createdAt2() {
      return  this.comment.created_at?.substr(11,8)
    },
  },
  methods: {
    ...mapActions(['deleteComment', 'updateComment']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    deleteC() {
      this.deleteComment({ commentPk: this.comment.pk , reviewPk: this.$route.params.reviewPk })
    },
    updateC() {
      this.updateComment(this.payload)
      this.isEditing = false
    }
  }
}
</script>

<style scoped>
.users {
  color: black;
  opacity: 0.8;
}

.users:hover {
  cursor: pointer;
  color: red;
  opacity: 0.8;
}
</style>