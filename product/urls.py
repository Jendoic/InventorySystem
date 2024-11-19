from rest_framework.routers import DefaultRouter
from .views import (ProductViewSet, StockMovementViewSet, 
                    SupplierViewSet, ReorderViewSet, 
                    StockMovementHistory, ProductSaleView,
                    WelcomeView)

from django.urls import path, include

router = DefaultRouter()

router.register('products', ProductViewSet, basename='product')
router.register('stock_movement', StockMovementViewSet, basename='stock_movement')
router.register('supplier', SupplierViewSet, basename='supplier')
router.register('reorder', ReorderViewSet, basename='reorder')

urlpatterns =[
    path('', include(router.urls)),
    path('stock-history/', StockMovementHistory.as_view()),
    path('product-sales/', ProductSaleView.as_view()),
    path('welcome/', WelcomeView.as_view()),
    
]