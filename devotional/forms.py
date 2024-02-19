from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.Form):
    title = forms.CharField(max_length=100)
    verse = forms.CharField(max_length=100, label="Bible Verse (e.g. John 3:16)")