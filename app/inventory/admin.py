from django.contrib import admin

from .models import Product, Purchase
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
     list_display = ( 'id', 'title', 'quantity'  )
     ordering = ("-id",)
    #  list_filter = ('created_at',)
     search_fields = ('month', )
     list_per_page = 10     

class PurchaseAdmin(admin.ModelAdmin):
     list_display = ( 'id', 'product', 'quantity'  )
     ordering = ("-id",)
    #  list_filter = ('created_at',)
     search_fields = ('month', )
     list_per_page = 10     


admin.site.register(Product, ProductAdmin)
admin.site.register(Purchase, PurchaseAdmin)
