from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def diseaseHealth(req):
    return HttpResponse(' Disease Health Working fine')

def pestDetection(req):
    return HttpResponse('Image recieved')