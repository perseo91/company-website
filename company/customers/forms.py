from django import forms 
from .models import Customers,Country
class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customers  
        fields=['first_name','last_name','address','cellphone','email','city']
    
class CountryForm(forms.ModelForm):
    class Meta:
        model=Country
        fields=['name']
    def clean_name(self):
        name=self.cleaned_data['name']
        if Country.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError(f"El Pais {name} ya esta registrado") 
        return name   