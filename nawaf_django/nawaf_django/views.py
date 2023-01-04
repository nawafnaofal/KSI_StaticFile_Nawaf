from nawaf_django import forms
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from blog.models import Post

def articles(request,year):
    year=year
    str=year
    return HttpResponse(year)

def index(request):
    context = {
        'heading' : 'Form Manual'
    }
    
    if request.method == 'POST':
        print("ini adalah method post")
        context['username'] = request.POST['username']
        context['address'] = request.POST['address']
    else:
        print("ini adalah method GET")
    
    return render(request, 'index.html', context)

def about(request):
    return HttpResponse("ini about")

def delete(request, id):
    Post.objects.filter(id=id).delete()
    return HttpResponseRedirect('/blog/')


def form(request):
    classform = forms.classform(request.POST or None)
        
    if request.method == 'POST':
        if classform.is_valid():
            classform.save()
            return HttpResponseRedirect('/blog/')
            

        context = {
            'heading':'Home',
            'classform': classform
        }
        return render(request, 'form.html', context)


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

