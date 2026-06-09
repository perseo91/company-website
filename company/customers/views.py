from django.shortcuts import render
from django.http import HttpResponse
from .models import Customers
from .forms import CustomerForm
def createCustomer(request):
    if request.method=="POST":
        form=CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'customers_form.html',{'form':form})
    else:
        form=CustomerForm()
        return render(request,'customers_form.html',{'form':form})
    

