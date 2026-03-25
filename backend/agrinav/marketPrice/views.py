from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def health(req):
    return HttpResponse("Application Working Fine")