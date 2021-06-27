from logging import PlaceHolder
from django import forms
from django.db import models
from django.db.models import fields
from tinymce import TinyMCE
from .models import Post , Comment
from marketing.models import contact


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Post
        fields = ('title' , 'overview' , 'content' , 'thumbnail' ,
        'categories' , 'featured' , 'previous_post' , 'next_post')

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class' : 'form-control',
        'placeholder' : 'Type your comment',
        'id' : 'usercomment',
        'rows' : '3'
    }))
    class Meta:
        model = Comment
        fields = ('content' , ) 


class ContactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = ('username' , 'email' , 'profile')