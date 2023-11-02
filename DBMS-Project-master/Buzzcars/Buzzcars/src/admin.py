from django.contrib import admin
from .models import Dealer, Vehicle, Customer, Sale, Tax

# Register your models here.
admin.site.register(Dealer)
admin.site.register(Vehicle)
admin.site.register(Customer)
admin.site.register(Sale)
admin.site.register(Tax)