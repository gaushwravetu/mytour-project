from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author','title','location','short_desc','full_desc','place_photo']

        widgets = {
            'author': forms.TextInput(attrs={'class':'form-control'}),
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'location': forms.TextInput(attrs={'class':'form-control'}),
            'short_desc': forms.TextInput(attrs={'class':'form-control'}),
            'full_desc': forms.Textarea(attrs={'class':'form-control'}),
        }