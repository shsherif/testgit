from django import forms
class Simpleform(forms.Form):
    firstname = forms.CharField(max_length=50)
    initials =forms.CharField(max_length=50)
    lastname = forms.CharField(max_length=50)
