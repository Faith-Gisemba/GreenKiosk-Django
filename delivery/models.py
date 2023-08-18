from django.db import models

# Create your models here.
class Delivery(models.Model):
    class Meta:
        verbose_name_plural = "deliveries"
    customer_name = models.CharField(max_length=100)
    delivery_address = models.CharField(max_length=200)
    delivery_status = models.CharField(max_length=50)
    delivery_date = models.IntegerField()
    delivery_method = models.CharField(max_length=50)
    order_id = models.CharField(max_length=50)
    delivery_cost = models.IntegerField()

    def __str__(self):
        return f"Delivery for Order {self.order_id} - Customer {self.customer_name}"
