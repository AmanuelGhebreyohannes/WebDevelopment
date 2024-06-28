from django import forms

class SearchForm(forms.Form):
    title = forms.CharField(label="", max_length=100,widget=forms.TextInput(attrs={'class': 'search','name': 'title', 'placeholder': 'Search Encyclopedia'}))

class NewPageForm(forms.Form):
    title = forms.CharField(label="", max_length=100,widget=forms.TextInput(attrs={'class': 'search','name': 'title', 'placeholder': 'Enter Title'}))
    content = forms.CharField(label="",widget=forms.Textarea(attrs={'class': 'textareaPage','name': 'content', 'placeholder': 'Enter Markdown Content'}))

class EditPageForm(forms.Form):
    title = forms.CharField(label="", max_length=100,widget=forms.TextInput(attrs={'class': 'search','name': 'title', 'placeholder': 'Enter Title'}))
    content = forms.CharField(label="",widget=forms.Textarea(attrs={'class': 'textareaPage','name': 'content', 'placeholder': 'Enter Markdown Content'}))

class MyForm(forms.Form):
    title = forms.CharField(label="", max_length=100,widget=forms.TextInput(attrs={'class': 'search','name': 'title', 'readonly': 'readonly'}))
    content = forms.CharField(label="",widget=forms.Textarea(attrs={'class': 'textareaPage','name': 'content', 'placeholder': 'Enter Markdown Content'}))