from django.db import models

# Create your models here.
class customer(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField()
    account_no = models.CharField(max_length=122)
    amount = models.IntegerField()
    def __str__(self):
        return self.name

class transaction_details(models.Model):
    user_name = models.CharField(max_length=122)
    user_accno = models.CharField(max_length=122)
    user_balance = models.IntegerField()
    user_deposit = models.IntegerField()
    destiname = models.CharField(max_length=122)
    date = models.DateTimeField()

