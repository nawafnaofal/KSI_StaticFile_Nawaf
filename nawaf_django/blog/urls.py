from django.urls import path, re_path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('recent/', views.recent, name='recent'),
    path('post/', views.recent, name='post'),
    re_path(r'^delete/(?P<id>[0-9]+)/$', views.delete, name='delete')
]
