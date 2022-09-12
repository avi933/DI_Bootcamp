from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('hello', views.hello, name='hello'),
    path('trial', views.trial, name='trial'),
    path('my_name', views.my_name, name='my_name')
]