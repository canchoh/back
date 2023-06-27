from django.db import models
from django.conf import settings
import uuid
from seller.models import Market

class Category(models.Model):
    categorykey = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    categoryforeignkey = models.ForeignKey(Market, on_delete=models.CASCADE)

    big_group = models.CharField(max_length=20)
    medium_group = models.CharField(max_length=20)
    small_group = models.CharField(max_length=20, blank= True, null= True)

class Inventory(models.Model):
    Inventorykey = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inventoryforeignkey = models.ForeignKey(Category, on_delete=models.CASCADE)
    barcode = models.IntegerField()
    Inventory_name = models.CharField(max_length=30)
    Inventory_price = models.IntegerField()
    origin=models.CharField(max_length=30)
    weight= models.CharField("무게(g)",max_length=20, blank= True, null= True)
    count= models.IntegerField("수량(갯수)",blank= True, null= True)
    manufacture = models.CharField(max_length=20)
    sale =models.BooleanField()










# Create your models here.
