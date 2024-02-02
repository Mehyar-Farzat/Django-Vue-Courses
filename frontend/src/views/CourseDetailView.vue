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
        <button type="button" class="btn btn-secondary mt-4 ">Enroll</button>      
      </div>
    </div>
  </div>
</template>

<script>
  import { courses } from '../tem-data'
  export default {
    name: 'CourseDetailPage',
    data(){
      return {
        course: courses.find(course => course.id == this.$route.params.course_id)
      }
    }
  }
</script>