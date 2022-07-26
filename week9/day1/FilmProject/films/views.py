from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def homepage(request):
    context={
        'films':Film.objects.all()
    }
    return render(request,'homepage.html',context)

def addFilm(request):
    context={
        'addfilm':AddFilmForm()
    }
    if request.method=="POST":
        form=AddFilmForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Error")
    return render(request,'addFilm.html ',context)

def addDirector(request):
    context={
        'form':AddDirectorForm()
    }
    if request.method=="POST":
        form=AddDirectorForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Error")
    return render(request,'addDirector.html ',context)