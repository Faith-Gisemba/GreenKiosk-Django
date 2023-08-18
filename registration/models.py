from django.db import models

# Create your models here.
class Signup(models.Model):
    class Meta:
        verbose_name_plural = "signup"
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    confirm_password=models.CharField(max_length=50)

    
    def register_customer(self):
        self.save
    def get_customer_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
    def isExist(self):
        if Customer.objects.filter(email = self.email):
            return True
        return False


class Login(models.Model):
    class Meta:
        verbose_name_plural = "login"
    user_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)


    def register_customer(self):
        self.save
    def get_customer_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
    def isExist(self):
        if Customer.objects.filter(email = self.email):
            return True
        return False
