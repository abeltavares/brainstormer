<template>
  <form @submit.prevent="submitIdea" class="input-group mb-3 idea-form">
    <input v-model="newIdeaText" placeholder="New idea" class="form-control" required />
    <button type="submit" class="btn btn-success ml-2">Add Idea</button>
  </form>
</template>

<script>
import axios from 'axios'

export default {
  props: ['sessionId'],
  data() {
    return {
      newIdeaText: ''
    }
  },
  methods: {
    submitIdea() {
      const newIdea = {text: this.newIdeaText, votes: 0}
      const baseURL = process.env.VUE_APP_API_BASE_URL
      axios.post(`${baseURL}/sessions/${this.sessionId}/ideas`, newIdea)
          .then(response => {
            this.$emit('idea-added', response.data)
            this.newIdeaText = ''
          })
          .catch(error => {
            console.error("There was an error adding the idea:", error)
          })
    }
  }
}
</script>

<style scoped>
.idea-form {
  display: flex;
  justify-content: space-between;
  margin-top: 10px;
}

.idea-form input {
  flex: 1;
  margin-right: 10px;
  padding: 8px;
  border-radius: 4px;
  border: 1px solid #ddd;
}

.idea-form button {
  padding: 8px 12px;
  border-radius: 4px;
  border: none;
  background-color: #28a745;
  color: #fff;
  cursor: pointer;
}

.idea-form button:hover {
  background-color: #218838;
}
</style>
