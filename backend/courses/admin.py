from django.contrib import admin
from .models import Category, Course

# Register your models here.

admin.site.register(Course)
admin.site.register(Category)