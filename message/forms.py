from .models import Tweet, TweetComment, Message, Contacts
from django import forms


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ('message', 'image')
            
    def save(self, commit=True, user_id=None):
        instance = (TweetForm, self).save(commit=False)
        if user_id:
            instance.author_id = user_id
        if commit:
            instance.save()
        return instance

class TweetCommentForm(forms.ModelForm):
    class Meta:
        model = TweetComment
        fields = ('body',)


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('sender', 'message',)
    
    def save(self, commit=True, user_id=None):
        instance = (MessageForm, self).save(commit=False)
        if user_id:
            instance.author_id = user_id
        if commit:
            instance.save()
        return instance

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ('friend',)
        
        def save(self, commit=True, user_id=None):
            instance = (ContactForm, self).save(commit=False)
            if user_id:
                instance.author_id = user_id
            if commit:
                instance.save()
            return instance