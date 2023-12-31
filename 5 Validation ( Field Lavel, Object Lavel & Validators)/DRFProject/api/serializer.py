from rest_framework import  serializers
from . models import Students


# VALIDATOR 

def start_with_f(value):
    if value[0].lower() != 'f':
        raise serializers.ValidationError('Name Must Be Start With F')
    return value


class StudentSerializers(serializers.Serializer):
    # id = serializers.IntegerField()
    name = serializers.CharField(max_length=100, validators=[start_with_f])
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
    
    #FILED LAVEL VALIDATION
    def validate_age(self,value):
        if value >=70:
            raise serializers.ValidationError('age must be under 70')
        return value
    
    # Object Lavel Validation
    def validate(self,data):
        name = data.get('name')
        country = data.get('country')
        if name.lower() == 'bezos' and country.lower() != 'usa':
            raise serializers.ValidationError('Country need to be USA')
        return data
    