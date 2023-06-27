from django.shortcuts import render
from rest_framework import viewsets, routers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpRequest
from .sarializer import *
from management.models import Category, Inventory
from django.http import JsonResponse


@api_view(['POST'])
def create_category(request):
    pass

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


category_list = CategoryViewSet.as_view({
    'get':'list',
    'post':'create',
})
category_detail = CategoryViewSet.as_view({
    'get':'retrieve',
    'patch':'p[partial_update',
    'delete':'destroy',
})
# Create your views here.



@api_view(['POST'])
# 재고 수량 증가
def increase_inventory(Inventorykey, count):
    product = Inventory.objects.get(id=Inventorykey)
    inventory= Inventory.objects.get_or_create(product=product)
    inventory.count += count
    inventory.save()

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


Inventory_list = InventoryViewSet.as_view({
    'get':'list',
    'post':'create',
})

Inventory_detail = InventoryViewSet.as_view({
    'get':'retrieve',
    'patch':'p[partial_update',
    'delete':'destroy',
})

# @api_view(['POST'])
# def increase_inventory(request):
#     pass
#
# class IncreaseViewSet(viewsets.ModelViewSet):
#     queryset = Inventory.objects.all()
#     serializer_class = increase_inventory
#
#
# Inventory_list = IncreaseViewSet.as_view({
#     'get':'list',
#     'post':'create',
# })
#
# Inventory_detail = IncreaseViewSet.as_view({
#     'get':'retrieve',
#     'patch':'p[partial_update',
#     'delete':'destroy',
# })
