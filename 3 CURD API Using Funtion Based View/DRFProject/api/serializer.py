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
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.gender = validated_data.get('gender',instance.gender)
        instance.country = validated_data.get('country',instance.country)
        instance.age = validated_data.get('age',instance.age)
        instance.save()
        return instance
