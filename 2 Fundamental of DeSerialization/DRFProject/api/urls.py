from django.urls import path, include
from . import views
urlpatterns = [
   path('student/', views.student_list, name='students'),
   path('student/<int:pk>/', views.student_details, name='student'),
   path('createstudent/', views.create_student, name='create_student'),
]