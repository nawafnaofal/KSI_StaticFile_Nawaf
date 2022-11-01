from django.http import HttpResponse
from django.shortcuts import render

def articles(request,year):
    year=year
    str=year
    return HttpResponse(year)

def index(request):
    return HttpResponse('ini index')

def about(request):
    return HttpResponse("ini about")