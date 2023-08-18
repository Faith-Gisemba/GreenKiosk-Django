from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category_images/')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    stock = models.PositiveIntegerField(default=0)