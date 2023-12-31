from django.urls import path, include
from . import views
urlpatterns = [
   path('student/<int:pk>/', views.StudentRtrUpdtDeltAPI.as_view(), name='student'),
   path('student/', views.StudentListCreateAPI.as_view(), name='students'),
   
]