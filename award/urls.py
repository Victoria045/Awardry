from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('profile', views.ProfileViewSet)

urlpatterns = [
    path('',views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login',auth_views.LoginView.as_view(), name='login'),
    path('account/', include('django.contrib.auth.urls')),
    path('profile/<username>/', views.profile, name='profile'),
]