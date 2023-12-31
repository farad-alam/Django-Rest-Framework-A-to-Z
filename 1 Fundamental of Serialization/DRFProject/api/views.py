from django.shortcuts import render
from . models import Students
from .serializer import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
# Create your views here.

# Single Instanece / Studnet Data
def student_list(request):
    student_obj = Students.objects.all()
    serializer = StudentSerializers(student_obj, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

# MULTIPLE INSTANCE >> WITH JSONrenderer
# def student_details(request,pk):
#     student_obj = Students.objects.get(id=pk)
#     serializer = StudentSerializers(student_obj)
#     json_data = JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data, content_type='application/json')

# MULTIPLE INSTANCE >> WITH JSONResponse
def student_details(request,pk):
    student_obj = Students.objects.get(id=pk)
    serializer = StudentSerializers(student_obj)
    return JsonResponse(serializer.data, safe=False)
