from rest_framework import serializers
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from user_app.models import User

class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = get_user_model()
        fields = ('email', 'password')
        extra_kwargs = {'password':{'write_only':True}}
    
    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)
    
    def update(self,instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user


