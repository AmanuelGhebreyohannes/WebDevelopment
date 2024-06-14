from django import forms

class SearchForm(forms.Form):
    title = forms.CharField(label="", max_length=100,widget=forms.TextInput(attrs={'class': 'search','name': 'title', 'placeholder': 'Search Encyclopedia'}))