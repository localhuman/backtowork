

from django import forms

from .models import Author

class TweetForm(forms.Form):

    sent_by = forms.ModelChoiceField(queryset=Author.objects.all(), widget=forms.HiddenInput())
    reply_to = forms.ModelChoiceField(queryset=Author.objects.all(), required=False)


