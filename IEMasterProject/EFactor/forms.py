from django import forms
from django.contrib.auth.forms import UserCreationForm



class PostFormEFactor(forms.Form):
    name = forms.CharField()
    grams = forms.FloatField()

class PostForm(forms.Form):
    name = forms.CharField()
    molarmass = forms.FloatField()
    concentration = forms.FloatField()



class MyForm(forms.Form):
    name = forms.CharField()
    grams = forms.CharField()


