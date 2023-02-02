from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework import serializers,validators


class LoginSerailizer(serializers.ModelSerializer):
    username = serializers.CharField(max_length = 30)
    password = serializers.CharField(max_length = 40)  
    
class RegSerializer(serializers.ModelSerializer):
    class Meta:
        Model = User
        fields = ['username','email','password']
