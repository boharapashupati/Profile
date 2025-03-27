from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'profiles', views.ProfileViewSet, basename='profile')

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('profile/set-avatar/', views.set_default_avatar, name='set_default_avatar'),
    path('register/', views.register, name='register'),
    
    path('api/', include(router.urls)),
    path('api/token/', views.CustomAuthToken.as_view(), name='api_token_auth'),
    path('api/search/', views.ProfileSearchView.as_view(), name='profile_search'),
] 