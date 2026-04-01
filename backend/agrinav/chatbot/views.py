from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def chatbotHealth(req):
    return HttpResponse("Health for chatbot working")