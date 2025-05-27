from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import Client,Shoes,Material,Production

class ShoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoes
        fields = '__all__'
        #exclude = ['id']
        
class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        #fields = '__all__'
        #fields =['type', 'description']
        exclude = ['isremoved']


class ClientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Client
        
        fields = '__all__'
       

class ProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Production
        #fields = ['tag','shoes','client','size','shoes_ammount']
        exclude = ['create_at','date_finished', 'finished']

