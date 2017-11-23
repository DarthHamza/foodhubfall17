from django import forms
from .models import Restaurant, Item

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = '__all__'
        exclude = ['slug']

        widgets = {
        	'opening_time' : forms.TimeInput(attrs={'type':'time'}),
        	'closing_time' : forms.TimeInput(attrs={'type':'time'}),
        }

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        exclude = ['slug']