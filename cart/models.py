from django.db import models
from refund.models import Refund

class Cart(models.Model):
    product_name = models.CharField(max_length=20)
    quantity = models.IntegerField()
    image = models.ImageField()
    price = models.IntegerField()
    date = models.DateTimeField()

    refund = models.ForeignKey(Refund, on_delete=models.CASCADE, null=True)

