from django.contrib import admin
from .models import Customers

admin.site.register(Customers)
# Register your models here.
class ModelCustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'address','cellphone','email','city') 
    list_display_links = ('first_name', 'last_name')          
    
    # Sidebar filters based on fields
    list_filter = ('address',)                 
    
    # Adds a search bar targeting specific fields
    search_fields = ('first_name', 'last_name')  
