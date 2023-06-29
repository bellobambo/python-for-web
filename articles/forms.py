from django import forms
from .import models

class CreateArticles(forms.ModelForm):
    thumb = forms.ImageField()
    class Meta:
        model = models.Article
        fields = ['title' , 'body' , 'slug' , 'thumb']
