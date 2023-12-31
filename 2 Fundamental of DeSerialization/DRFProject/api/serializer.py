from rest_framework import  serializers
from . models import Students
class StudentSerializers(serializers.Serializer):
    # id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    gender = serializers.CharField(max_length=50)
    country = serializers.CharField(max_length=50)
    age = serializers.IntegerField()

    def create(self, validate_data):
        return Students.objects.create(**validate_data)
