from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Product)
class Products_details(admin.ModelAdmin):
    list_display = ['ID','name','category','brand','description','price','created_at','image','pdfs']
    list_filter = ['category','price']
    search_fields = ['name','brand']
    ordering = ['ID']
    list_per_page = 20