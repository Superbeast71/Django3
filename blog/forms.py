from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    required_css_class = 'my-custom-class'
    title = forms.CharField(max_length=20)

    class Meta:
        model = Post
        fields = ['title', 'author', 'post_type', 'category', 'text']

