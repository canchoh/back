from rest_framework import serializers
from .models import Category, Inventory
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = \
            '__all__'

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = \
            '__all__'
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = \
            '__all__'

class DeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = \
            '__all__'





# 재고 수량 증가
def increase_inventory(Inventorykey, count):
    product = Inventory.objects.get(id=Inventorykey)
    inventory= Inventory.objects.get_or_create(product=product)
    inventory.count += count
    inventory.save()

# 재고 수량 감소
def decrease_inventory(Inventorykey, count):
    product = Inventory.objects.get(id=Inventorykey)
    inventory = Inventory.objects.get(product=product)
    inventory.count -= count
    inventory.save()



