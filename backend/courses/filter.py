from django_filters import rest_framework as filters
from .models import Course
import django_filters



class CourseFilter(filters.FilterSet):    # create filter class 
    class Meta:  
        model = Course    
        fields = { 
            
            
            'price': ['range'],
            'category': ['exact'],

        }