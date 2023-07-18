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
from django.http import HttpResponseNotAllowed
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

# @api_view(['POST'])
# def product(request):
#     # 'sale'이 True인 제품들을 조회합니다.
#     queryset = Inventory.objects.filter(sale=True)
#
#     # 조회한 제품들을 시리얼라이저에 전달하여 직렬화합니다.
#     serializer = ProductSerializer(queryset, many=True)
#
#     # 직렬화된 데이터를 응답합니다.
#     return Response(serializer.data)




@api_view(['GET', 'POST'])
def product(request):
    if request.method == 'GET':
        # Retrieve products for which 'sale' is True.
        queryset = Inventory.objects.filter(sale=True)

        # Pass the retrieved products to the serializer to serialize them.
        serializer = ProductSerializer(queryset, many=True)

        # Response serialized data.
        return Response(serializer.data)

    elif request.method == 'POST':
        # Handle POST request (same as the original code).
        queryset = Inventory.objects.filter(sale=True)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)









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

from django.shortcuts import get_object_or_404

@api_view(['GET', 'DELETE'])
def delete(request):
    if request.method == 'DELETE':
        json_data = json.loads(request.body)
        for item in json_data:

            barcode = item.get('barcode')





        queryset = Inventory.objects.filter(barcode=barcode).delete()
        serializer = DeleteSerializer(queryset, many=True)

        # Response serialized data.
        return Response(serializer.data)



    elif request.method == 'GET':
        queryset= Inventory.objects.all()
        serializer = DeleteSerializer(queryset, many=True)

        # Response serialized data.
        return Response(serializer.data)





@api_view(['DELETE'])
def delete_inventory(request, barcode):
    inventory = get_object_or_404(Inventory, id=id)

    # 권한 검사 (예: 해당 Inventory에 대한 권한 확인)
    if not request.user.has_perm('app.delete_inventory'):
        # 권한이 없는 경우 에러 응답 반환
        return HttpResponse(status=403)

    # Inventory 삭제
    inventory.delete()

    # 삭제 완료 메시지 또는 다른 응답 반환
    return HttpResponse("Inventory 삭제 완료")






# def delete(request, Inventorykey):
#     # Inventory 객체가 존재하지 않을 경우 404 응답 반환
#     delete_inventory = get_object_or_404(Inventory, id=Inventorykey)
#
#     # 권한 및 인증 검사
#     if not request.user.is_authenticated:
#         # 인증되지 않은 사용자일 경우 401 Unauthorized 응답 반환
#         return HttpResponse(status=401)
#
#     # 권한 검사 (예: 해당 Inventory에 대한 권한 확인)
#     if not request.user.has_perm('app.delete_inventory'):
#         # 권한이 없는 경우 403 Forbidden 응답 반환
#         return HttpResponse(status=403)
#
#     # Inventory 삭제
#     delete_inventory.delete()
#
#     # 삭제 완료 메시지 또는 다른 응답 반환
#     return HttpResponse("Inventory 삭제 완료")
#

@csrf_exempt
def updete(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        print(json_data)

        for item in json_data:

            barcode = item.get('barcode')
            count = item.get('count')

    Inventory.objects.filter(barcode=barcode).update(count=count)


    return HttpResponse("Inventory 수정 완료")  # 빈 HttpResponse 객체 반환





        # serializer = InventorySerializer(data={'barcode': barcode, 'count': count})
        # if serializer.is_valid():
        #     serializer.save()

    #     return HttpResponse('Data saved successfully.')
    # else:
    #
    #     return HttpResponse('Invalid request method.')













