from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'category', views.CategoryViewSet)
router.register(r'inventory', views.InventoryViewSet)
# router.register(r'increase', views.IncreaseViewSet)

urlpatterns = [
    path('router/', include(router.urls)),
    path('update/', views.updete, name='update'),



]
