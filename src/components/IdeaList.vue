<template>
  <div class="idea-list">
    <ul>
      <li v-for="idea in sortedIdeas" :key="idea.id" class="idea-item">
        <IdeaItem :idea="idea" :sessionId="sessionId" @session-updated="updateSession" />
      </li>
    </ul>
  </div>
</template>

<script>
import IdeaItem from './IdeaItem.vue'

export default {
  props: ['ideas', 'sessionId'],
  components: { IdeaItem },
  computed: {
    sortedIdeas() {
      return this.ideas.slice().sort((a, b) => a.id - b.id); // Sort by ID or any other criteria
    }
  },
  methods: {
    updateSession(updatedSession) {
      this.$emit('session-updated', updatedSession)
    }
  }
}
</script>

<style scoped>
.idea-list {
  margin-top: 10px;
}

.idea-item {
  background-color: #fff;
  padding: 10px;
  border-radius: 8px;
  margin-bottom: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
</style>

<style scoped>
.idea-list {
  margin-top: 10px;
}

.idea-item {
  background-color: #fff;
  padding: 10px;
  border-radius: 8px;
  margin-bottom: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
</style>
