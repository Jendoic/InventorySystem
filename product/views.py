from django.shortcuts import get_object_or_404
from django.db import transaction, models



from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView


from .serializers import ProductSerializer, StockMovementSerializer, SupplierSerializer,  ReorderSerializer
from .models import Product, StockMovement, Supplier, Reorder

class WelcomeView(APIView):
   
    
    def get(self, request):
        api_list = [
            'Product List: /api/v1/products/<int:pk>/',
            'Stock Movement history: /api/v1/stock-history/',
            'Supplier List: /api/v1/suppliers/',
            'Supplier Detail: /api/v1/suppliers/<int:pk>/',
            'Reorder history: /api/v1/reorder/',
            'Product Sales: /api/v1/product-sales/',
            
            
            
        ]
        return Response({"message": "Welcome to the API"
                         , "api_list": api_list})


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    
    
    @action(detail=False, methods=['get'], url_path='low_stocks')
    def low_stocks(self, request):
        low_stock_products = Product.objects.filter(stock_quantity__lte=models.F('low_stock_threshold'))
        
        serializer = self.get_serializer(low_stock_products, many=True)
        return Response(serializer.data)
    
    
class StockMovementViewSet(viewsets.ModelViewSet):
    queryset = StockMovement.objects.all()
    serializer_class = StockMovementSerializer
    permission_classes = [IsAuthenticated]
    
    
    def perform_create(self, serializer):
        product = get_object_or_404(Product, pk=serializer.validated_data.get('product').id)
        quantity_added = serializer.validated_data.get('quantity_added')
        quantity_removed = serializer.validated_data.get('quantity_removed')
        print("quantity:", quantity_added)
        movement_type = serializer.validated_data.get('movement_type')

        with transaction.atomic():  
            if movement_type == 'IN':
                product.stock_quantity += int(quantity_added)
            elif movement_type == 'OUT':
                if product.stock_quantity < int(quantity_removed):
                    raise ValidationError("Insufficient stock to remove")
                product.stock_quantity -= int(quantity_removed)
            product.save()
        
        serializer.save()
        
        
    
    
class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]
    
    
class ReorderViewSet(viewsets.ModelViewSet):
    queryset = Reorder.objects.all()
    serializer_class = ReorderSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_update(self, serializer):
        instance = serializer.save()
        if instance.status == Reorder.Status.COMPLETED:
            product = instance.product
            product.stock_quantity += instance.quantity
            product.save()
            
            
class StockMovementHistory(ListAPIView):
    queryset = StockMovement.objects.all()
    serializer_class = StockMovementSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product', 'movement_type', 'timestamp']
    
    
    

class ProductSaleView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        sales = StockMovement.objects.filter(movement_type='OUT')\
            .values('product__name')\
                .annotate(total_sales=models.Sum('quantity_removed'))\
                    .order_by('-total_sales')
        return Response(sales)