from django import forms

class SearchQueryForm(forms.Form):
	search = forms.CharField()
