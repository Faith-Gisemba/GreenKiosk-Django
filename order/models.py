from django.db import models
from customer.models import Customer
from delivery.models import Delivery
from cart.models import Cart

# Create your models here.
class Order(models.Model):

    customer = models.ForeignKey(Customer,null=True,on_delete=models.CASCADE)
    deliver = models.OneToOneField(Delivery,null=True,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='orders')
    

    order_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    items = models.CharField(max_length=255)
    order_status = models.CharField(max_length=50)

    def __str__(self):
        return f"Order {self.order_id} - User {self.user_id}"
