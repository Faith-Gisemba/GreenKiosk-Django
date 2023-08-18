from django.db import models

# Create your models here.
class Ticket(models.Model):
    class Meta:
        verbose_name_plural = "ticket"
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=15)
    customer_name = models.CharField(max_length=32)
    items_description = models.TextField()
    frequently_asked_questions = models.TextField()
    help_center = models.TextField()
    feedback_and_suggestions = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

