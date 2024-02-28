from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.id = kwargs.pop('id', None)
        super(CommentForm, self).__init__(*args, **kwargs)
        
        if self.id:
            try:
                comment = Comment.objects.get(pk=self.id)
                # Populate the form fields with data from the comment instance
                self.fields['body'].initial = comment.body
            except Comment.DoesNotExist:
                pass

    class Meta:
        model = Comment
        fields = ('body',)
