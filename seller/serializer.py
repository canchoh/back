from rest_framework import serializers
from .models import Seller, Ceo, Business, Market
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator

# class SellerloginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Seller
#         fields = \
#             '__all__'
#         # fields = ['business_number','seller_email','seller_password']
#
class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = \
            '__all__'

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = \
            '__all__'

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ceo
        fields = \
            '__all__'

class CeoSerializer(serializers.ModelSerializer):
    ceo_email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Ceo.objects.all())],
        # 이메일에 대한 중복 검증하기
    )
    ceo_password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],  # 비밀번호에 대한 검증하기 >조건 넣는 방법
    )
    ceo_password2 = serializers.CharField(write_only=True, required=True)

    # 비밀번호 확인을 위한 필드

    class Meta:
        model = Ceo  # 모델은 User을
        fields = \
        '__all__'

    def validate(self, data):  # 추가적으로 password와 password2가 일치 여부 확인
        if data['ceo_password'] != data['ceo_password2']:
            raise serializers.ValidationError(
                {"ceo_password": "password fields didn't match."})  # 일치하지 않다면
        return data

class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = \
            '__all__'

    # def create(self, validated_data):
    #     ceo = Ceo.objects.create_user(
    #         username=validated_data['ceo_name'],
    #         email=validated_data['ceo_email'],
    #     )

# class StoreSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Store
#         fields = ('store_name','store_number','store_address', 'store_type','store_content','business_number_store',)