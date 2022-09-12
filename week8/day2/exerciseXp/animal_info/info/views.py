from multiprocessing import context
from django.shortcuts import render
from .models import *


def families(request):
    family = Family.objects.all()
    context = {'families':family}
    return render(request, 'family.html',context)

def animal(request, id):
    animal = Animal.objects.all()
    # filtered = animals.filter(id=id)
    filtered = Animal.objects.get(pk=id)
    context = {'animal' : animal}
    return render(request, 'animal.html',context)

def animals(request):
    animals = Animal.objects.all()
    filtered = Animal.objects.get(id = id)
    context = {'animals' : animal}
    return render(request, 'animals.html',context)

