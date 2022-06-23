from pydoc import classname
from rest_framework import serializers
from .models import Job, Application
from users.models import User
from users.serializers import UserSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'job_title', 'description', 'salary', 'type', 'recruiter']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['recruiter'] = UserSerializer(instance.recruiter).data
        return representation
    


class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'