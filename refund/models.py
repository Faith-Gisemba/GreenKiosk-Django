from django.db import models

class Refund(models.Model):
    reason = models.CharField(max_length=200)
    refund_amount = models.DecimalField(max_digits=10, decimal_places=2)
    processed_date = models.DateTimeField(auto_now_add=True)

    


    


