from django import forms 
from .models import Customers,Country,Region,City
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
    
class RegionForm(forms.ModelForm):
    class Meta:
        model=Region
        fields=['name','country']
    def clean_name(self):
        name=self.cleaned_data['name']
        if Region.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError(f"La región {name} ya esta registrada") 
        return name     
class CityForm(forms.ModelForm):
    class Meta:
        model=City
        fields=['name','region']
    def clean_name(self):
        name=self.cleaned_data['name']
        if City.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError(f"La ciudad {name} ya esta registrada") 
        return name  