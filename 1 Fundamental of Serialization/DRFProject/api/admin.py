from django.contrib import admin
from . models import Students
# Register your models here.

@admin.register(Students)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','gender','country','age']