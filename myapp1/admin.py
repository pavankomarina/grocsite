from django.contrib import admin

# Register your models here.
from myapp1.models import *
admin.site.register(Type)
admin.site.register(Item)
admin.site.register(Client)
admin.site.register(OrderItem)


