
<template>

<body :class="{'dark': darkMode}">
  <navbar :darkMode="darkMode" @dark-mode-change="toggleDarkMode"/>

    <RouterView />

</body>
</template>

<script>

import { RouterLink, RouterView } from 'vue-router'
import navbar from './components/navbar.vue';

export default {
  name: 'App',
  components: {
    navbar,
  },
  data() {
    return {
      darkMode: false
    }
  },
  mounted() {
    this.darkMode = localStorage.getItem('darkMode') === 'true';
  },

  methods: {
    toggleDarkMode(darkMode) {

      this.darkMode = darkMode;
      localStorage.setItem('darkMode', this.darkMode);
      
    }
  }

  
}
</script>

<style>
html.dark, 
body.dark {
  background-color: black;
  color: white;
}
</style>
