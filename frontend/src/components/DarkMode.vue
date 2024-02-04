<template>

    <button class="btn btn-primary" @click="toggleDarkMode"> </button>


</template>


<script>
    export default {
        name: "DarkMode",
        props: {
            darkMode: {
                type: Boolean,
                default: false
            }
        },
        methods: {
            toggleDarkMode() {
                this.$emit('dark-mode-change',!this.darkMode);
            }
        }
    }

</script>