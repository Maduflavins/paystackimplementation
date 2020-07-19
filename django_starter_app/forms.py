from django import forms
from .models import Purchase


class PurchaseForm(forms.ModelForm):
	name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Name'}))
	address = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}))
	amount = forms.FloatField(required=False, widget=forms.NumberInput())
	email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class':'form-control'}))

	class Meta():
		model = Purchase
		fields = '__all__'