from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from .models import Customers,Country
from .forms import CustomerForm,CountryForm
def createCustomer(request):
    if request.method=="POST":
        form=CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'customers_form.html',{'form':form})
    else:
        form=CustomerForm()
        return render(request,'customers_form.html',{'form':form})
def createCountry(request):
    if request.method=="POST":
        countryform=CountryForm(request.POST)
        if countryform.is_valid():
            pais=countryform.save()
            
            messages.success(request,f"El pais '{pais.name}' fue registrado con exito")
            
            return render(request,'countries_form.html',{'countryform':countryform})
    else:    
        countryform=CountryForm()
    return render(request,'countries_form.html',{'countryform':countryform  })


