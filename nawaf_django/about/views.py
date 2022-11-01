from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("ini index about")
# Create your views here.
