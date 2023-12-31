from .models import Students
from .serializer import StudentSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(['GET','POST','PUT','DELETE'])
def student_api(request, pk=None):

    if request.method == 'GET':
        id = pk
        if id is not None:
            student = Students.objects.get(pk=id)
            serializer = StudentSerializers(student)
            return Response(serializer.data)
        all_student = Students.objects.all()
        serializer = StudentSerializers(all_student, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created!!!','status': status.HTTP_201_CREATED, 'data':serializer.data})
        return Response(serializer.errors)
    
    if request.method == 'PUT':
        id = pk
        get_student_by_id = Students.objects.get(pk=id)
        serializer = StudentSerializers( get_student_by_id ,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated!!!','status': status.HTTP_202_ACCEPTED, 'data':serializer.data})
        return Response(serializer.errors)
    
    if request.method == 'DELETE':
        id = pk
        student = Students.objects.get(pk=id)
        student.delete()
        return Response({'msg':'Successfully deleted data'})

