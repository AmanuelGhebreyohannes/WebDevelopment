from django import forms

class PlaceBids(forms.Form):
    
    bid_value = forms.DecimalField(label="Bid")

    
class createListingForm(forms.Form):
    OPTIONS = (
        ('Fashion', 'Fashion'),
        ('Toys', 'Toys'),
        ('Electronics', 'Electronics'),
        ('Home', 'Home'),
        ('Other', 'Other'),
    )
    title = forms.CharField(label="", max_length=100,widget=forms.TextInput(attrs={'class': 'title','name': 'title', 'placeholder': 'Enter item name: '}))
    description = forms.CharField(label="",max_length=500,widget=forms.Textarea(attrs={'class': 'description','name': 'description', 'placeholder': 'Enter description'}))
    start_bid_value = forms.DecimalField(label="start vid value $")
    image_url = forms.URLField()
    category =forms.ChoiceField(choices=OPTIONS)




    