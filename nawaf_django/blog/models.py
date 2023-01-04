
import email
from django import forms
from django.db import models
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.text import slugify 
# from blog.models import Post

from nawaf_django.validators import title_val

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255,
    validators = [title_val])
    body = models.TextField()
    email = models.EmailField(blank=True)
    slug = models.SlugField(blank=True, editable=False)
    
    def save(self):
        self.slug = slugify(self.title)
        super(Post,self).save()
    def __str__(self):
        return "{}".format(self.title)
    
