from django.shortcuts import render
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
#from .filter import CourseFilter


from .serializers import CourseSerializer, CategorySerializer
from .models import Course, Category


# Create your views here.

class CourseListFilterAPI(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['price', 'category']
    #filterset_class = CourseFilter


class CategoryListAPI(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer