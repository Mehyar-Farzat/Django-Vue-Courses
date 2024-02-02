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
  export default {
    name: 'CourseFilter',
    data(){
      return {
        category:[
        {id:1 , name:'Web Development'},
        {id:2 , name:'Software Development'},
        {id:3 , name:'Machine Learning'},
        {id:4 , name:'Mobile Development'},
        ],
        selectedCategory: []
      }
    },
    watch:{
      selectedCategory(){
        this.$emit('category-updated', this.selectedCategory)
      }
    }
  }
</script>

<style>
.form-check-input{
  margin-right: 15px;
}
</style>