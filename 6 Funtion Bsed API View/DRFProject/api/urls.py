from django.urls import path, include
from . import views
urlpatterns = [
   path('student/<int:pk>/', views.student_api, name='students'),
   path('student/', views.student_api, name='students'),
   
]