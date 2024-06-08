<template>
  <div class="idea-item-container d-flex justify-content-between align-items-center">
    <div class="flex-grow-1 d-flex align-items-center">
      <p class="mb-0 mr-2">{{ idea.text }}</p>
      <span class="votes-box d-flex align-items-center justify-content-center">{{ idea.votes }}</span>
    </div>
    <div class="button-group d-flex">
      <button @click="voteIdea" class="btn btn-primary btn-sm mr-2">Vote</button>
      <button @click="deleteIdea" class="btn btn-danger btn-sm">Delete</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  props: ['idea', 'sessionId'],
  methods: {
    voteIdea() {
      const baseURL = process.env.VUE_APP_API_BASE_URL;
      axios.post(`${baseURL}/sessions/${this.sessionId}/ideas/${this.idea.id}/vote`)
        .then(response => {
          this.$emit('session-updated', response.data)
        })
        .catch(error => {
          console.error("There was an error voting for the idea:", error);
        });
    },
    deleteIdea() {
      const baseURL = process.env.VUE_APP_API_BASE_URL;
      axios.delete(`${baseURL}/sessions/${this.sessionId}/ideas/${this.idea.id}`)
        .then(response => {
          this.$emit('session-updated', response.data)
        })
        .catch(error => {
          console.error("There was an error deleting the idea:", error);
        });
    }
  }
}
</script>

<style scoped>
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.idea-item-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  border-radius: 4px;
  border: 1px solid #ddd;
  margin-bottom: 5px;
  background-color: #fff;
  animation: fadeIn 1s ease;
}

.idea-item-container:hover {
  background-color: #f9f9f9;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.idea-item-container p {
  margin: 0;
  flex-grow: 1;
  color: #333;
  margin-right: 10px;
}

.votes-box {
  background-color: #f0f0f0;
  border: 1px solid #ccc;
  border-radius: 4px;
  padding: 3px 8px;
  margin-right: 10px;
  font-weight: bold;
  color: #333;
}

.button-group {
  display: flex;
  gap: 10px;
}

.button-group button {
  padding: 5px 10px;
  border-radius: 4px;
  border: none;
  cursor: pointer;
}

.button-group .btn-primary {
  background-color: #007bff;
  color: #fff;
}

.button-group .btn-primary:hover {
  background-color: #0056b3;
}

.button-group .btn-danger {
  background-color: #dc3545;
  color: #fff;
}

.button-group .btn-danger:hover {
  background-color: #c82333;
}
</style>
