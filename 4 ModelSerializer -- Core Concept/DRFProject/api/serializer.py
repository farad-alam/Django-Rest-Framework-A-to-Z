from rest_framework import  serializers
from . models import Students


class StudentModelSerializer(serializers.ModelSerializer):

    # VALIDATOR 
    def start_with_f(value):
        if value[0].lower() != 'f':
            raise serializers.ValidationError('Name Must Be Start With F')
        return value
    
    # readonly fields
    name = serializers.CharField(validators=[start_with_f])


    class Meta:
        model= Students
        fields = ['id','name','gender','country','age']
        read_only_fields = ['name']
        # fields = '__all__'
        # exclude = ('gender')


    #FILED LAVEL VALIDATION
    def validate_age(self,value):
        if value >=70:
            raise serializers.ValidationError('age must be under 70')
        return value
    

    # Object Lavel Validation
    # def validate(self,data):
    #     name = data.get('name')
    #     country = data.get('country')
    #     if name and country is not None:
    #         if name.lower() == 'bezos' and country.lower() != 'usa':
    #             raise serializers.ValidationError('Country need to be USA')
    #         return data






    