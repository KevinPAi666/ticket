from django.db import models

# Create your models here.
class order_model(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=255)
    address = models.JSONField()
    price = models.IntegerField()
    currency = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.id} | {self.name} | {self.address} | {self.price} | {self.currency}"
