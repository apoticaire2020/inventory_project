from django.contrib import admin
from .models import Product
from django.contrib.auth.models import Group
from import_export.admin import ImportExportModelAdmin 

admin.site.site_header = 'Senhaj inventary'

class ProductAdmin(admin.ModelAdmin):
    list_display=('designation' , 'category' , 'forme' ,'ppv' ,'pph', 'quantity' ,)
    list_filter=('category','forme',)
    

# Register your models here.

admin.site.register(Product , ProductAdmin)
# admin.site.unregister(Group)



