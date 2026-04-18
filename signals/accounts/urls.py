from django.urls import path, include
from .models import *
from .serializers import *
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('register', RegisterView, basename='register')
router.register('profile', ProfileView, basename='profile')

urlpatterns = [
    path('', include(router.urls)),
]
