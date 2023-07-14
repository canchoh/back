from django.shortcuts import render
from rest_framework import viewsets, routers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpRequest
from .sarializer import *
from management.models import Category, Inventory
from django.http import JsonResponse
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
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

# @csrf_exempt
# def updete(request):
#     if request.method == 'POST':
#         json_data = json.loads(request.body)
#         Inventory.save()
#         print(json_data)
#
#         response_data = {'message': 'Data received successfully.'}
#
#         return JsonResponse(response_data)

@api_view(['POST'])
def updete(request, barcode):
    barcode = Inventory.objects.get(id= barcode)
    count = request.POST['count']
    barcode.save()

    response_data = {'message': 'Data received successfully.'}

    return JsonResponse(response_data)







