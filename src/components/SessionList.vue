<template>
  <div class="session-list">
    <h2 class="mb-4">Sessions</h2>
    <ul class="list-group list-group-flush">
      <li v-for="session in sessions" :key="session.id" class="list-group-item mb-3">
        <SessionItem :session="session" :sessionId="session.id" @update-session="updateSession" @delete-session="deleteSession" />
      </li>
    </ul>
    <form @submit.prevent="addSession" class="input-group mt-4">
      <input v-model="newSessionTitle" placeholder="New session title" class="form-control" required />
      <button type="submit" class="btn btn-primary ml-2">Add Session</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import SessionItem from './SessionItem.vue'

export default {
  components: { SessionItem },
  data() {
    return {
      sessions: [],
      newSessionTitle: ''
    }
  },
  created() {
    this.fetchSessions()
  },
  methods: {
    fetchSessions() {
      const baseURL = process.env.VUE_APP_API_BASE_URL;
      axios.get(`${baseURL}/sessions`)
          .then(response => {
            this.sessions = response.data
          })
          .catch(error => {
            console.error("There was an error fetching the sessions:", error);
          });
    },
    addSession() {
      const baseURL = process.env.VUE_APP_API_BASE_URL;
      const newSession = {title: this.newSessionTitle, ideas: []}
      axios.post(`${baseURL}/sessions`, newSession)
          .then(response => {
            this.sessions.push(response.data)
            this.newSessionTitle = ''
          })
          .catch(error => {
            console.error("There was an error adding the session:", error);
          });
    },
    updateSession({id, session}) {
      const index = this.sessions.findIndex(s => s.id === id)
      if (index !== -1) {
        this.sessions.splice(index, 1, session)
      }
    },
    deleteSession(sessionId) {
      const baseURL = process.env.VUE_APP_API_BASE_URL;
      axios.delete(`${baseURL}/sessions/${sessionId}`)
          .then(() => {
            this.sessions = this.sessions.filter(session => session.id !== sessionId)
          })
          .catch(error => {
            console.error("There was an error deleting the session:", error);
          });
    }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Fredoka+One&display=swap');

body {
  font-family: 'Fredoka One', cursive;
}

.session-list {
  margin-bottom: 20px;
  padding: 20px;
  background-color: #e9ecef;
  border-radius: 8px;
  transition: transform 0.3s;
}

.session-list:hover {
  color: #2d2d2d; /* Slightly darker text color */
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1); /* Small box-shadow for "lift" effect */
}

h2 {
  font-size: 2rem;
  color: #343a40;
}
</style>
