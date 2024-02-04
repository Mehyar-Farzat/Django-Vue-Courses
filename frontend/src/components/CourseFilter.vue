<template>
  <div class="container">
    <h3>Courses Filter</h3>
    <form>
      <div class="mt-4">
        <label for="" class="cat-label">Filter by Category</label>
        <div class="cat-checkbox" v-for="cat in category" :key="cat.id">
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
 .cat-label{
  font-size: 1.2rem;
    font-weight: 300;
    color: #8898aa;
  }

  .cat-checkbox{
    margin-bottom: 0.5rem;
    align-items: center;
    justify-content: space-between;
    margin-top: 10px;

  }

  .form-label{
    margin-left: 4px;
  }
</style>