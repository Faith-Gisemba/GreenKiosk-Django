from django.db import models

# Create your models here.

class Payment(models.Model):
    payment_id = models.IntegerField(primary_key=True)
    customer_id = models.IntegerField()
    payment_method = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=50)
    payment_date = models.IntegerField()
    payment_amount = models.IntegerField()
    currency_used = models.CharField(max_length=50)

    def __str__(self):
        return f"Payment {self.payment_id} - Customer {self.customer_id}"
