from django.shortcuts import render
from rest_framework import viewsets, routers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpRequest
from .serializer import *
from seller.models import Seller
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken

@api_view(['POST'])
def login_api(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    seller = serializer.validated_data['seller']

    _, token = AuthToken.objects.create(seller)
    return Response({
        'seller_info': {
            'business_number' : seller.seller.business_number,
            'username': seller.seller_email

        },
        'token' :token
    })


@api_view(['POST'])
def Sign_Up(request):
    # try:
        serializer = SellerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            result = {'result' : serializer.data}
            return JsonResponse(result, status=201)
        else:
            result = {'result' : serializer.errors}
            return JsonResponse(result, status=400)

    # except keyError:
    #     return JsonResponse({'result' : 'Key error'}, status=400)

@api_view(['GET','POST'])
def Seller_s(request):
    queryset = Seller.objects.all()

    serializer = SellerloginSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def Seller_detail(request, seller_pk):
    check = get_object_or_404(Seller, pk=seller_pk)
    serializer = SellerSerializer(check)
    return Response(serializer.data)

api_view(['POST'])
def create_seller(request):
    pass

class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


seller_list = SellerViewSet.as_view({
    'get':'list',
    'post':'create',
})
seller_detail = SellerViewSet.as_view({
    'get':'retrieve',
    'patch':'p[partial_update',
    'delete':'destroy',
})

# class StoreViewSet(viewsets.ModelViewSet):
#    queryset = Store.objects.all()
#    serializer_class = StoreSerializer
# Create your views here.
