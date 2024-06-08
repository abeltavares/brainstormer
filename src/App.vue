<template>
  <div id="app" class="d-flex flex-column min-vh-100">
    <header class="mb-4 text-center">
      <div class="lightbulb-animation">
        <svg
          id="lightbulb"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 64 64"
          width="64px"
          height="64px"
        >
          <path
            fill="#FFEB3B"
            d="M32,4C18.745,4,8,14.745,8,28c0,7.733,3.73,14.567,9.5,19.023V52c0,1.104,0.896,2,2,2h1v2 c0,2.209,1.791,4,4,4h13c2.209,0,4-1.791,4-4v-2h1c1.104,0,2-0.896,2-2v-4.977C52.27,42.567,56,35.733,56,28C56,14.745,45.255,4,32,4 z"
          />
          <path
            fill="#607D8B"
            d="M29 59H35V63H29zM24 53H40V57H24zM19 50H45V52H19z"
          />
        </svg>
      </div>
      <h1 class="text-center">Brainstormer</h1>
    </header>
    <main class="flex-grow-1 container">
      <SessionList />
    </main>
    <footer class="text-center py-2">
      <p class="mb-0">&copy; 2024 Abel Tavares</p>
    </footer>
  </div>
</template>

<script>
import SessionList from './components/SessionList.vue';

export default {
  name: 'App',
  components: {
    SessionList,
  },
};
</script>

<style scoped>
body {
  background-color: #f8f9fa;
  font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
  margin: 0; /* Remove default margin */
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.lightbulb-animation {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 10px;
  padding-top: 20px;
}

@keyframes pulse {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.1);
  }
  100% {
    transform: scale(1);
  }
}

#lightbulb {
  animation: pulse 2s infinite;
}

h1 {
  font-size: 2.5rem;
  color: #343a40;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  padding-top: 5px;
  padding-bottom: 20px;
}

header, main, footer {
  width: 100%;
}

main {
  padding: 0 15px;
}

footer {
  background-color: #343a40;
  color: #fff;
  padding: 5px 0; /* Reduced padding */
}
</style>
