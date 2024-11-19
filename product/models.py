import random
from django.db import models
from django.utils.translation import gettext_lazy as _

class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    sku = models.CharField(max_length=20, unique=True, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)
    low_stock_threshold = models.PositiveIntegerField(default=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-timestamp"]
        indexes = [
        models.Index(fields=['name']),
    ]
    
    def generate_sku(self):
        return f"PRD{random.randint(1000, 9999)}"

    def is_low_stock(self):
        return self.stock_quantity <= self.low_stock_threshold
    
        
    def save(self, *args, **kwargs):
        if not self.sku:
            while True:
                potential_sku = self.generate_sku()
                if not Product.objects.filter(sku=potential_sku).exists():
                    self.sku = potential_sku
                    break
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name
    
    

class StockMovement(models.Model):
    
    class MovementType(models.TextChoices):
        none = ""
        IN = "IN"
        OUT = "OUT"
        
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="stock_movements")
    quantity_added = models.IntegerField(null=True, blank=True)
    quantity_removed = models.IntegerField(null=True, blank=True)
    movement_type = models.CharField(max_length=10, choices=MovementType, default=MovementType.none)
    timestamp = models.DateTimeField(auto_now_add=True)
    reason = models.CharField(max_length=255, null=True)
    def __str__(self):
        return f"{self.product.name} - {self.timestamp}"




class Supplier(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    products = models.ForeignKey(Product, related_name='suppliers', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Reorder(models.Model):
    
    class Status(models.TextChoices):
        PENDING = "Pending", _('Pending')
        COMPLETED = "Completed", _('Completed')
        CANCELLED = "Cancelled", _('Cancelled')
        
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reorders')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='reorders')
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=20,
                              choices=Status.choices,
                              default=Status.PENDING,
                              )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Reorder for {self.product.name} (Quantity: {self.quantity})"