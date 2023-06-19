from django.contrib import admin
from .models import Seller, Business, Ceo, Market

admin.site.register(Seller)
admin.site.register(Business)
admin.site.register(Ceo)
admin.site.register(Market)

# admin.site.register(Store)
# Register your models here.
