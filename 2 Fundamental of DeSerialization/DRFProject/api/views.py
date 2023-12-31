from django.shortcuts import render
from .models import Students
from .serializer import StudentSerializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
import io
from django.views.decorators.csrf import csrf_exempt

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

# 
# Deserialization View
@csrf_exempt
def create_student(request):
    if request.method == 'POST':
        json_data = request.body
        print(json_data)
        stream = io.BytesIO(json_data)
        print(stream)
        python_data = JSONParser().parse(stream)
        print(python_data)
        serialize = StudentSerializers(data=python_data)
        print(serialize)
        if serialize.is_valid():
            serialize.save()
            res = {'msg':'New Student Created Succecfylly'}
            json_res = JSONRenderer().render(res)
            return HttpResponse(json_res, content_type='application/json')
        json_res = JSONRenderer().render(serialize.errors)
        # res = {'msg':'New Student not Created Succecfylly'}
        # json_res = JSONRenderer().render(res)
        return HttpResponse(json_res, content_type='application/json')