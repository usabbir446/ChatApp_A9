from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('msg', views.msg, name='msg'),
]
