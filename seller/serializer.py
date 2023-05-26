from rest_framework import serializers
from .models import Seller

class SellerloginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = \
            '__all__'
        # fields = ['business_number','seller_email','seller_password']

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = \
            '__all__'

# class StoreSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Store
#         fields = ('store_name','store_number','store_address', 'store_type','store_content','business_number_store',)