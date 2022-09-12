from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def hello(request):
    return render(request, "hello.html", {})

def trial(request):
    return render(request, "trial.html", {})

def my_name(request):
    context = {
        "users": [
            {
                "username" : "Avishek",
                "fav food" : ["Burger","mine bouille"],
                "mobile_phone":{
                "make": "samsung",
                "phone_number": "545235534" 
                                }
            },
            {
                "username" : "Jayesh",
                "fav food" : ["mine","dhall puri"],
                "mobile_phone":{
                "make": "apple",
                "phone_number": "54673443"}
            },
            {
                "username" : "Nayar",
                "fav food" : ["Burger","piza"],
                "mobile_phone":{
                "make": "Redmi",
                "phone_number": "5456964"
                                }
            }
        ]

        

        
        
    }
    return render (request, "my_name.html",context)