
<template>
  <navbar/>
  <RouterView />
</template>

<script>

import { RouterLink, RouterView } from 'vue-router'
import navbar from './components/navbar.vue';

export default {
  name: 'App',
  components: {
    navbar
  }
}
</script>

