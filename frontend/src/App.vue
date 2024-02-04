
<template>
  <navbar :darkMode="darkMode" />
  <Router>
    <RouterLink to="/"></RouterLink>
    <RouterView />

  </Router>
  
</template>

<script>

import { RouterLink, RouterView } from 'vue-router'
import navbar from './components/navbar.vue';

export default {
  name: 'App',
  components: {
    navbar
  },
  data() {
    return {
      darkMode: false
    }
  },
  
}
</script>

