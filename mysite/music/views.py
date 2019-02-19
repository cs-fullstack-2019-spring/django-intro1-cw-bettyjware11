from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Defining function to be called when the url is requested
# this function will return the bad request text
def index(request):
    return HttpResponse("This is a bad request. Start with the music route.")
# this function returns an Alicia Keys Song
def AliciaKeys(request):
    return HttpResponse("Songs in A Minor")

# this function returns a JCole song
def  JCole(request):
    return HttpResponse("Middle Child")

# this function returns a Tupac song
def Tupac(request):
    return HttpResponse("Mackaveli")