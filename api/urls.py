"""untitled2 URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from login import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

#  the token authentication created by rest frame work simple jwt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts', include('login.urls')),  # to insert urls.py file from login directory
    path('api-auth/', include('rest_framework.urls')),  # from rest framework for authentication login button
    path('api/token/', TokenObtainPairView.as_view()),  # to obtain token for user per request
    path('', views.hello.as_view(), name='hello'),  # to get hello class
    path('api/token/refresh', TokenRefreshView.as_view()),  # to refresh the token
]
