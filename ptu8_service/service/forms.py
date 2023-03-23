from django import forms 
from . import models

class CustomerForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = '__all__'


        
