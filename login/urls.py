from django.urls import path
from . import views

# to call hello class in login.views

urlpatterns = [
    path('', views.hello.as_view(), name='hello')
]
