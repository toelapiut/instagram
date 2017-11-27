from .models import *
from django import forms 

class NewArticleForm(forms.ModelForm):
    class Meta:
        model= Article
        exclude=['pub_time','user']


class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        exclude=['pub_time','user','article']