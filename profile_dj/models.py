from custom_user.models import User
from django.db import models

# Create your models here.
class Account_detail(models.Model):

    ID_CHOICES = [
        ('idcard', 'ID Card'),
        ('passport', 'Passport'),
    ]

    MARITAL_CHOICES = [
        ('married', 'Married'),
        ('widowed', 'Widowed'),
        ('separated', 'Separated'),
        ('divorced', 'Divorced'),
        ('single', 'Single'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, default="")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    id_type = models.CharField(max_length=20, choices=ID_CHOICES)
    id_number = models.IntegerField()
    marital_status = models.CharField(max_length=20, choices=MARITAL_CHOICES)
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
    
class Bank_detail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bank_name =  models.CharField(max_length=100)
    bank_number = models.IntegerField()
    bank_account = models.CharField(max_length=100)
    bank_branch = models.CharField(max_length=100)