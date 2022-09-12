from django.contrib import admin
from .models import Animal, Family #import the Person model

# Register your models here.
admin.site.register(Family)
admin.site.register(Animal)

