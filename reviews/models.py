from django.db import models

# Create your models here.
class Review(models.Model):
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Review by {self.comment}"


