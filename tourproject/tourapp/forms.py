from django import forms
from . models import Toy


class toy_form(forms.ModelForm):
    class Meta:
        model=Toy
        fields=['name','price','img']
