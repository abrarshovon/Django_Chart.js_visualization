from django.db import models

# Create your models here.
class JsonModel(models.Model):
    date= models.DateField(null=True)
    trade_code= models.TextField(null=True)
    high=models.TextField(null=True)
    low=models.TextField(null=True)
    open= models.TextField(null=True)
    close=models.TextField(null=True)
    volume= models.TextField(null=True)
    def __str__(self):
        return self.trade_code