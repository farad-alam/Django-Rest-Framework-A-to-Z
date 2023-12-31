from .models import Students
from .serializer import StudentSerializers
from rest_framework.generics import GenericAPIView,ListAPIView,RetrieveAPIView,\
UpdateAPIView,CreateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView

# Create your views here.


class StudentListAPi(ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializers
    
class StudentRUDApi(RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializers




