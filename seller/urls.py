from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from rest_framework.routers import DefaultRouter
from . import views





router = DefaultRouter()
router.register(r'sellerData', views.SellerViewSet)
router.register(r'signup',views.CeoViewSet)
router.register(r'check', views.BusinessViewSet)
router.register(r'market', views.MarketViewSet)
# router.register(r'store', views.StoreViewSet)
# # router.register(r'sellerapi', StoreAPI, basename='Store')
# # router.register('seller/login', views.LoginViewSet)


urlpatterns = [
    # path('seller/', views.test),
    # path('', include(router.urls)),
    # path('', views.Seller_s),
    path('', include(router.urls)),
    path('check/',views.Check),
    path('signup/', views.Sign_UP),
    # path('create/', views.create_seller),
    # path('<int:check_pk>', views.Seller_detail),
    # path('login/', views.login_api),
    # path('sign_up/', views.Sign_Up)




]