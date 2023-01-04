from django import forms
from django.shortcuts import render
from .models import Post
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

# def articles(request,year):
#     year=year
#     str=year
#     return HttpResponse(year)


def index(request):
    db = Post.objects.all()
    context = {
        'title':'Blog',
        'heading':'Blog',
        'subheading':'postingan',
        'post': db,
    }
    return render (request, 'blog/index.html', context)

def recent(request):
    return HttpResponse("RECENT")

# def post(request):
#     return HttpResponse("ini pos")

def delete(request, id):
    Post.objects.filter(id=id).delete()
    return HttpResponseRedirect('/blog/')

def update(request, id):
    updt = Post.objects.get(id=id)
    data = {
        'title' : updt.title,
        'body' : updt.body,
        'email' : updt.email,
    }
    classform = forms.classform(request.POST or None, initial=data, instance=updt)
    
    if request.method =='POST':
        if classform.is_valid():
            classform.save()
            return HttpResponseRedirect('/blog/')
        
        
    context = {
        'heading':'Updt',
        'classform': classform
    }
    return render(request, 'form.html', context)
