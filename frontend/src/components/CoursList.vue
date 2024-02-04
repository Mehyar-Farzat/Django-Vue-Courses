<template>
<div class="row mt-5">
  <div class="col-lg-4" v-for="course in courses" :key="courses.id">

    <Card style="overflow: hidden" class="course-card">
        <template #header>
            <img alt="user header" class="course-img" :src="course.image" />
        </template>
        <template #title>{{course.name}}</template>
        <template #subtitle>{{ course.category }}</template>
        <template #content>
            <p class="m-0">
                {{course.subtitle}}
            </p>
        </template>
        <template #footer>
            <div class="flex gap-3 mt-1">
                
                <Button label="Course Details" class="w-full" />
            </div>
        </template>
    </Card>
  
  </div>
</div>
</template>

<script>

  
  export default {
    name: 'CourseList',
    props: ['courses']
  }
</script>


<style>
.course-img {
  max-width: 100%;
  height: 15vw;
  object-fit: cover;
  object-position: center;
  border-radius: 10px 10px 10px 10px;
  


    
}

.course-card {
  box-sizing: border-box;
  max-width: 100%;
  height: auto;
  padding: 20px;
  margin: 10px 0px;
}
</style>