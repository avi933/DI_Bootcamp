from django.urls import path 
from . import views 

# one urlpattern per line
urlpatterns = [
    path('animal/<int:id>', views.animal, name='animal'),
    path('animals', views.animals, name='animals'),
    path('family', views.family, name='family'),
]