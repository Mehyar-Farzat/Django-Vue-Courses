<template>
    <nav class="navbar navbar-expand-lg bg-dark" data-bs-theme="dark">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Learn</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarColor02" aria-controls="navbarColor02" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarColor02">
      <ul class="navbar-nav me-auto">
        <li class="nav-item">
            <RouterLink class="nav-link active" to="/">Courses</RouterLink>
            <span class="visually-hidden">(current)</span>

        </li>
      </ul>
      <DarkMode :darkMode="darkMode" @dark-mode-change="toggleDarkMode" />    
    </div>
  </div>
    </nav>
</template>
  
<script>
    import DarkMode from './DarkMode.vue';

    export default {     
      name: 'Navbar',   
      components: {     
        DarkMode
      },
      props: {        // props are used to pass data from parent to child
        darkMode:{    // darkMode is a prop
          type: Boolean,
          default: false
        }

      },
      methods: {
        toggleDarkMode(){
          this.$emit('dark-mode-change',!this.darkMode);
        }
      }
    }

</script>