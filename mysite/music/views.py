from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("This is a bad request. Start with the music route.")

def AliciaKeys(request):
    return HttpResponse("Songs in A Minor")


def  JCole(request):
    return HttpResponse("Middle Child")


def Tupac(request):
    return HttpResponse("Mackaveli")