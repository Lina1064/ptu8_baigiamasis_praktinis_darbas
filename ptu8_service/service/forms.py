from django import forms 
from . import models

class CustomerForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = '__all__'

class UserOrderCreateForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = ('customer', 'status',)
        widgets = {
            'status': forms.HiddenInput(),
        }
        
