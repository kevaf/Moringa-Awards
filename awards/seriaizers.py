from rest_framework import serializers
from .models import Profile, Projects

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'bio', 'info')

class ProjectsSerializer(serializers.serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('title', 'description', 'link', 'user')