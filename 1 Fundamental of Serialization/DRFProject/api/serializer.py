from rest_framework import  serializers

class StudentSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    gender = serializers.CharField(max_length=50)
    country = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
