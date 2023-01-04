# classform forms.classform(request.POST or None)
from django import forms
from django.http import HttpResponse

from blog.models import Post


# if request.method == 'POST':
#     if clasform.is_valid():
#         Post.objects.create(
#             title = classform.cleaned_data.get('title'),
#             body = classform.cleaned_data.get('body'),
#             email = classform.cleaned_data.get('email'),
#         )
#     return HTTPResponseRedirect('/blog/')

class classform(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'body',
            'email',
        ]
        
        widget={
            'title': forms.TextInput(
                attrs = {
                    'class' : 'form',
                    'placeholder':'Masukan Judul',
                }
            )
        }
        
   

def clean_title(self):
    ji = self.cleaned_data.get('title')
    
    if ji == "Rasis":
        raise forms.ValidationError("Can't post Rasis")
    
    return ji