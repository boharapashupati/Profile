from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')
        read_only_fields = ('id',)

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    completion_percentage = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ('id', 'user', 'bio', 'location', 'birth_date', 'avatar',
                 'phone_number', 'facebook_url', 'twitter_url', 'linkedin_url',
                 'skills', 'education', 'work_experience', 'last_login',
                 'profile_views', 'completion_percentage')
        read_only_fields = ('id', 'last_login', 'profile_views')

    def get_completion_percentage(self, obj):
        return obj.get_completion_percentage()

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('bio', 'location', 'birth_date', 'avatar',
                 'phone_number', 'facebook_url', 'twitter_url', 'linkedin_url',
                 'skills', 'education', 'work_experience') 