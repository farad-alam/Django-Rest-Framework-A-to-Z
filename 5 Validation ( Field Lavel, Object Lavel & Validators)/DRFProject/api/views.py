from django.shortcuts import render
from .models import Students
from .serializer import StudentSerializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
import io
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class student_api(View):

    def get(self,request,*args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        if id is not None:
            student_data = Students.objects.get(id=id)
            serialize = StudentSerializers(student_data)
            python_to_json_data = JSONRenderer().render(serialize.data)
            return HttpResponse(python_to_json_data, content_type='application/json')
        all_students = Students.objects.all()
        serialize = StudentSerializers(all_students,many=True)
        python_to_json_data = JSONRenderer().render(serialize.data)
        return HttpResponse(python_to_json_data, content_type='application/json')
    
    def post(self,request,*args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serialize = StudentSerializers(data=python_data)
        if serialize.is_valid():
            serialize.save()
            res = {'msg':'New Student Created successfully!!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serialize.errors)
        return HttpResponse(json_data, content_type='application/json')
    
    def put(self,request,*args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        if id is not None:
            student_data = Students.objects.get(id=id)
            serialize = StudentSerializers( student_data, data=python_data, partial=True)
            if serialize.is_valid():
                serialize.save()
                res = {'msg':'Student Updated successfully!!'}
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data, content_type='application/json')
            python_to_json_data = JSONRenderer().render(serialize.errors)
            return HttpResponse(python_to_json_data, content_type='application/json')






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