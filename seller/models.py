from django.db import models
from django.conf import settings
import uuid
# from user.models import User

class Seller(models.Model):

    business_number = models.CharField(max_length=15, primary_key=True)
    seller_email = models.EmailField(max_length=45, blank=False)
    seller_name = models.CharField(max_length=20, blank=False)
    seller_birthday = models.CharField(max_length=20, blank=False)
    seller_address = models.CharField(max_length=40,blank=False)
    seller_phone = models.CharField(max_length=15, blank=False)
    seller_password = models.CharField(max_length=30, blank=False)

class Business(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    business = models.CharField("사업자번호",max_length=20, blank=False)



# Create your models here.
class Ceo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,)

    ceo_business = models.ForeignKey(Business, on_delete=models.CASCADE)
    ceo_email = models.EmailField(max_length=45, blank=False)
    ceo_name = models.CharField(max_length=20, blank=False)
    ceo_birthday = models.CharField(max_length=20, blank=False)
    ceo_address = models.CharField(max_length=40, blank=False)
    ceo_phone = models.CharField(max_length=15, blank=False)
    ceo_password = models.CharField(max_length=30, blank=False)
    ceo_password2 = models.CharField(max_length=30, blank=False)

class Market(models.Model):
    marketkey = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,)
    market_ceo= models.ForeignKey(Ceo, on_delete=models.CASCADE)
    market_number = models.CharField(max_length=15)

    market_address = models.CharField(max_length=70)
    market_type = models.CharField(max_length=20)
    market_content = models.CharField(max_length=500)
    market_name = models.CharField(max_length=45, blank=True, null=True)













    # def __str__(self):
    #     return self.business_number

# seller = Seller(business_number='11-1111-12', seller_email='als946581750@naver.com',
#                 seller_name='양수민', seller_birthday='2000-09-22',seller_address='서울시', seller_phone='010-2296-5817', seller_password='PW1234')
# # blank = False : null값 허용 X
# seller.save()


# class Store(models.Model):
#     store_name = models.CharField(max_length=20, blank=False, primary_key= True)
#     business_number_store = models.ForeignKey(Seller, on_delete=models.CASCADE)
#     store_number = models.CharField(max_length=13, blank=False)
#     store_address = models.CharField(max_length=40, blank=False)
#     store_type = models.CharField(max_length=20, blank=True, null=True)
#     store_content = models.CharField(max_length=255, blank=True, null=True)

# # blank=True, null=True : null값 허용 O
#
# class Notification(models.Model):
#     business_number_notification= models.ForeignKey(Seller, on_delete=models.CASCADE)
#     seller_email_notification=models.ForeignKey(Seller, on_delete=models.CASCADE)
#     not_datetime=models.DateTimeField(auto_now = True, blank=False)
#     not_message=models.CharField(max_length=255, blank=False)
#
#
# class Category(models.Model):
#     category_id=models.CharField(max_length=15, blank=False, primary_key= True)
#     business_number_category= models.ForeignKey(Store, on_delete=models.CASCADE)
#     big_group=models.CharField(max_length=20, blank=False)
#     small_group=models.CharField(max_length=20, blank=True, null=True)
#     medium_group=models.CharField(max_length=20, blank=False)
#
# class Inventory(models.Model):
#     barcode= models.IntegerField(blank=False, primary_key= True)
#     category_id_inventory= models.ForeignKey(Category, on_delete=models.CASCADE)
#     product_name=models.CharField(max_length=20, blank=False)
#     product_price= models.IntegerField(blank=False)
#     origin=models.CharField(max_length=20, blank=False)
#     weight=models.CharField(max_length=15,blank=True, null=True)
#     count=models.CharField(max_length=15, blank=True, null=True)
#     manufacture=models.DateTimeField(blank=False)
#
# class Product(models.Model):
#     product_id=models.CharField(max_length=20, blank=False)
#     barcode_product=models.ForeignKey(Inventory, on_delete=models.CASCADE)
#     category_id_product=models.ForeignKey(Inventory, on_delete=models.CASCADE)
#     product_name=models.CharField(max_length=20, blank=False)
#     product_price= models.IntegerField(blank=False)
#     origin=models.CharField(max_length=20, blank=False)
#     weight=models.CharField(max_length=15,blank=True, null=True)
#     count=models.CharField(max_length=15, blank=True, null=True)
#     manufacture=models.DateTimeField(blank=False)
#
# class Consumer(models.Model):
#     consumer_email=models.CharField(max_length=45,  primary_key= True, blank=False)
#     product_id_consumer = models.ForeignKey(Product, on_delete=models.CASCADE)
#     consumer_name= models.CharField(max_length=20,  blank=False)
#     consumer_birthday =models.DateTimeField(blank=False)
#     consumer_phone=models.CharField(max_length=15, blank=False)
#     consumer_address=models.CharField(max_length=40, blank=False)
#     consumer_password=models.CharField(max_length=30, blank=False)
#
# class Cart(models.Model):
#     consumer_email_consumer=models.ForeignKey(Consumer, on_delete=models.CASCADE)
#     product_id_consumer=models.ForeignKey(Consumer, on_delete=models.CASCADE)
#     product_name= models.CharField(max_length=20, blank=False)
#     product_count= models.IntegerField(blank=False)
#     product_price= models.IntegerField(blank=False)



# Create your models here.
