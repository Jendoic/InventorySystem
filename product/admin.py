from django.contrib import admin

from .models import Product, StockMovement, Supplier, Reorder

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock_quantity', 'low_stock_threshold', 'timestamp')
    list_filter = ('name', 'price')
    search_fields = ('name', 'description')
    ordering = ('name',)

admin.site.register(Product, ProductAdmin)  


class StockMovementAdmin(admin.ModelAdmin):
    list_display = ('product', 'movement_type', 'quantity_added', 'quantity_removed','timestamp')
    list_filter = ('product', 'movement_type')
    search_fields = ('product__name', 'movement_type')
    ordering = ('product',)
    
admin.site.register(StockMovement, StockMovementAdmin)


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'timestamp')
    list_filter = ('name', )
    search_fields = ('name',)
    ordering = ('name',)
    
admin.site.register(Supplier, SupplierAdmin)


class ReorderAdmin(admin.ModelAdmin):
    list_display = ('product', 'supplier', 'quantity', 'status')
    list_filter = ('product', 'supplier')
    search_fields = ('product', 'supplier')
    ordering = ('status',)
    
admin.site.register(Reorder, ReorderAdmin)