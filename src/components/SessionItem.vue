<template>
  <div class="session-item-container card p-3 mb-3">
    <div class="d-flex justify-content-between align-items-center mb-3">
      <h3 class="mb-0">{{ session.title }}</h3>
      <button @click="deleteSession" class="btn btn-danger btn-sm">Delete Session</button>
    </div>
    <IdeaForm :sessionId="sessionId" @idea-added="addIdea"/>
    <IdeaList :ideas="localSession.ideas" :sessionId="sessionId" @session-updated="updateSession"/>
  </div>
</template>

<script>
import IdeaForm from './IdeaForm.vue'
import IdeaList from './IdeaList.vue'

export default {
  props: ['session', 'sessionId'],
  components: {IdeaForm, IdeaList},
  data() {
    return {
      localSession: JSON.parse(JSON.stringify(this.session))
    }
  },
  methods: {
    addIdea(idea) {
      this.localSession.ideas.push(idea)
      this.$emit('update-session', {sessionId: this.sessionId, session: this.localSession})
    },
    updateSession(updatedSession) {
      this.localSession = updatedSession
      this.$emit('update-session', {sessionId: this.sessionId, session: this.localSession})
    },
    deleteSession() {
      this.$emit('delete-session', this.sessionId)
    }
  },
  watch: {
    session: {
      handler(newSession) {
        this.localSession = JSON.parse(JSON.stringify(newSession))
      },
      deep: true
    }
  }
}
</script>

<style scoped>
.session-item-container {
  background-color: #f1f1f1;
  padding: 15px;
  border-radius: 8px;
}

h3 {
  margin-bottom: 10px;
  color: #007BFF;
}
</style>

<style scoped>
.session-item-container {
  background-color: #f1f1f1;
  padding: 15px;
  border-radius: 8px;
}

h3 {
  margin-bottom: 10px;
  color: #007BFF;
}
</style>
