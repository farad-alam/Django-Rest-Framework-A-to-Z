from rest_framework import  serializers
from . models import Students


# VALIDATOR 

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'
    