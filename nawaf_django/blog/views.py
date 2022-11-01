from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

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
