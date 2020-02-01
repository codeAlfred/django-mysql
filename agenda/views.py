from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def backend(request):
    return HttpResponse("Hello,back end")

def welcome(request):
    return HttpResponse("Hello, welcome")

def hi(request):    
    data={
        "status":"success",
        "mensaje":"helloo!!!!!",
        "error":"",
        }
    return HttpResponse(data)