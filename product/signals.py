from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

from .models import StockMovement, Reorder

@receiver(post_save, sender=StockMovement)
def check_and_create_reorder(sender, instance, **kwargs):
    product = instance.product
    if product.stock_quantity <= product.low_stock_threshold:
        if not Reorder.objects.filter(product=product, status=Reorder.Status.PENDING).exists():
            supplier = product.suppliers.first()
            if supplier:
                Reorder.objects.create(product=product, 
                                       supplier=supplier, 
                                       quantity=product.low_stock_threshold - product.stock_quantity + 10,
                )


@receiver(post_save, sender=Reorder)
def send_reorder_notification(sender, instance, created, **kwargs):
    if created:
        subject = f"Reorder Needed: {instance.product.name}"
        message = {
            f"A reorder has been created for the following product:\n"
            f"Product: {instance.product.name}\n"
            f"Quantity: {instance.quantity}\n"
            f"Supplier: {instance.supplier.name}\n"
            f"Status: {instance.status}\n\n"
            f"Please log in to manage this reorder."
        }
        recipient_list = ['hezekiaholajide3@gmail.com']  
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)