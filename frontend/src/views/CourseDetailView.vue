<template>
  <div class="container">
    <div class="row my-5">
      <div class="col-lg-3">
        <img :src="course.image" class="img-fluid"  alt="">
      </div>
      <div class="col-lg-9">
        <h2>{{ course.name }}</h2>
        <h5>{{ course.category }}</h5>
        <p>{{ course.price }}$</p>
        <p>{{ course.description }}</p>
        <button type="button" class="btn btn-secondary mt-4 ">Enroll</button>      
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

  export default {
    name: 'CourseDetailPage',
    data(){
      return {
        course: null
      }
      
    },
    created(){
      this.getCourse()
    },
    methods:{
      getCourse(){
        const courses_id = this.$route.params.course_id
        axios.get(`http://127.0.0.1:8000/courses/${courses_id}/api`)
        .then(response => {
          this.course = response.data;
         })

      }
    }
    }
  
</script>

