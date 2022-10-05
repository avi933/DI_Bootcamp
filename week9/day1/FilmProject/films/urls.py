from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('homepage/',views.homepage,name='homepage'),
    path('addFilm/',views.addFilm,name='addFilm'),
    path('addDirector/',views.addDirector,name='addDirecto'),
]