from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from django.core.files import File
from django.conf import settings
from django.utils import timezone
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import User
import os
import shutil
from .models import Profile
from .forms import ProfileForm, UserRegistrationForm
from .serializers import UserSerializer, ProfileSerializer, ProfileUpdateSerializer

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! Please complete your profile.')
            return redirect('profile_edit')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile_view(request):
    profile = request.user.profile
    # Update last login time
    profile.update_last_login()
    # Increment profile views
    profile.profile_views += 1
    profile.save()
    
    context = {
        'profile': profile,
        'completion_percentage': profile.get_completion_percentage(),
    }
    return render(request, 'profiles/profile.html', context)

@login_required
def profile_edit(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profiles/profile_edit.html', {'form': form})

@login_required
def set_default_avatar(request):
    profile = request.user.profile
    if not profile.avatar:
        # Create media directory if it doesn't exist
        avatar_dir = os.path.join(settings.MEDIA_ROOT, 'avatars')
        os.makedirs(avatar_dir, exist_ok=True)
        
        # Copy the default avatar to the user's profile
        default_avatar_path = os.path.join(settings.MEDIA_ROOT, 'default_avatar.jpg')
        user_avatar_path = os.path.join(avatar_dir, f'{request.user.username}_avatar.jpg')
        shutil.copy(default_avatar_path, user_avatar_path)
        
        # Set the avatar field
        relative_path = os.path.join('avatars', f'{request.user.username}_avatar.jpg')
        profile.avatar = relative_path
        profile.save()
    
    return redirect('profile')

# API Views
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                         context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
            'email': user.email
        })

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update']:
            return ProfileUpdateSerializer
        return ProfileSerializer

    @action(detail=False, methods=['get'])
    def me(self, request):
        profile = self.get_queryset().first()
        serializer = self.get_serializer(profile)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def update_avatar(self, request):
        profile = self.get_queryset().first()
        if 'avatar' not in request.FILES:
            return Response(
                {'error': 'No avatar file provided'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        profile.avatar = request.FILES['avatar']
        profile.save()
        serializer = self.get_serializer(profile)
        return Response(serializer.data)

class ProfileSearchView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        query = request.GET.get('q', '')
        if not query:
            return Response({'error': 'Search query is required'}, 
                          status=status.HTTP_400_BAD_REQUEST)
        
        profiles = Profile.objects.filter(
            user__username__icontains=query
        ) | Profile.objects.filter(
            bio__icontains=query
        ) | Profile.objects.filter(
            skills__icontains=query
        )
        
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
