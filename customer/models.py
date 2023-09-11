from django.db import models

class Customer(models.Model):
    id = models.AutoField(primary_key=True, default=0)  # Add the default value here
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"







