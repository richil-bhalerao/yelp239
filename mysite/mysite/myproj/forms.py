from django import forms
import datetime

class CategoryForm(forms.Form):
    email = forms.EmailField(required=True)
    description = forms.CharField(required=True)
    #creationDate = forms.DateField(initial=datetime.date.today)
    creationDate = forms.CharField(required=True)
    status = forms.CharField()
    
    