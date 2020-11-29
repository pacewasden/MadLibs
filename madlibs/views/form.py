from django import forms
from .models import Words

class WordForm(forms.ModelForm):
    class Meta:
        model = Words
        fields = ['noun','adjective','place','expression']