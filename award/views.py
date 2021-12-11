from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .models import Profile
from .serializers import ProfileSerializer
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
import random

def index(request):

    return render(request, 'award/index.html')

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer