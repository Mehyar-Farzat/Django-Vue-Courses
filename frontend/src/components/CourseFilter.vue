<template>
  <div class="container">
    <h3>Course Filter</h3>
    <form>
      <div class="mt-4">
        <label for="" class="mb-4">Filter by Category</label>
        <div v-for="cat in category" :key="cat.id">
          <input type="checkbox"
          :value="cat.id"
          class="form-check-input"
          :id="cat.id"
          v-model="selectedCategory"
          >
          <label :for="cat.id" class="form-label">{{ cat.name }}</label>
        </div>
      </div>
    </form>
  </div>
  
</template>

<script>

import axios from 'axios'
  export default {
    name: 'CourseFilter',
    data(){
      return {
        category:[],
        selectedCategory: []
      }
    },
    watch:{
      selectedCategory(){
        this.$emit('category-updated', this.selectedCategory)
      }
    },

    created(){
      this.getCategory()
    },
    methods:{
      getCategory(){
        axios.get("http://127.0.0.1:8000/category/api")
        .then(response => {
          this.category = response.data ;
          
        })
      }
    }
  }
</script>

<style>
.form-check-input{
  margin-right: 15px;
}
</style>