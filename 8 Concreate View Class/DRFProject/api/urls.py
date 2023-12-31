from django.urls import path, include
from . import views
urlpatterns = [
   # path('student/<int:pk>/', views.StudentRtrUpdtDeltAPI.as_view(), name='student'),
   path('student/', views.StudentListAPi.as_view(), name='students'),
   path('studentup/<int:pk>/', views.StudentRUDApi.as_view(), name='students'),
   
]