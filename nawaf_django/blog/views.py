from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    db = Post.objects.all()
    context = {
        'title':'Blog',
        'heading':'Blog',
        'subheading':'postingan',
        'post': db,
    }
    return render (request, 'blog/index.html', context)
