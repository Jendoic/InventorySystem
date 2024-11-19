from rest_framework import serializers

from .models import Product, StockMovement, Supplier, Reorder


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  
        

class StockMovementSerializer(serializers.ModelSerializer):
    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("Quantity must be greater than zero.")
        return value
    
    class Meta:
        model = StockMovement
        fields = '__all__'  
        

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
        
        
class ReorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reorder
        fields = '__all__'