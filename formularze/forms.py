from django import forms
from .models import Snippet

""""""

class ContactForm(forms.Form):

    """ pobiera z Forms """

    name = forms.CharField()
    email = forms.EmailField(label='E-mail')
    category = forms.ChoiceField(choices=[
        ('question', 'Question'),
        ('other', 'Other')
        ])
    subiect = forms.CharField(required=True)
    body = forms.CharField(widget=forms.Textarea)


class SnippetForm(forms.ModelForm):

    """ pobiera z ModelForm """
    
    class Meta:
        model = Snippet
        fields = ('name', 'body')
