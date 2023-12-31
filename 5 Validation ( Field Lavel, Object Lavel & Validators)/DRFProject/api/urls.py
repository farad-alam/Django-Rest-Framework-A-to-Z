from django.urls import path, include
from . import views
urlpatterns = [
   path('student/', views.student_api.as_view(), name='students'),
   
]