from django import forms
from blog.models import Post, Email
from django.forms import TextInput


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ('email',)
        widgets = {
            'email': TextInput(attrs={'class': 'form-control', 'placeholder': "example@foo.com"})
        }
