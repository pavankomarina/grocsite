from tabnanny import verbose
from django.db import models

# Create your models here.
from django.db import models 

import datetime

from django.contrib.auth.models import User

from django.utils import timezone

class Type(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Item(models.Model):
    type = models.ForeignKey(Type, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    stock = models.PositiveIntegerField(default=100)
    available = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    interested = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.name
    
    def topup(self):
        self.stock += 200
        self.save()

class Client(User):     
    CITY_CHOICES = [
        ('WD', 'Windsor'),
        ('TO', 'Toronto'),
        ('CH', 'Chatham'),
        ('WL', 'WATERLOO'),
    ]
    shipping_address = models.CharField(max_length=300, null=True, blank=True)
    city=models.CharField(max_length=2, choices=CITY_CHOICES, default='CH')
    interested_in = models.ManyToManyField(Type)
    phone_number = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
    
    class Meta:
        verbose_name="Client"
    
class OrderItem(models.Model):
    ORDER_STATUS = [
        (0, 'CANCELLED'),
        (1, 'PLACED'),
        (2, 'SHIPPED'),
        (3, 'DELIEVERED'),
    ]
    item = models.ForeignKey(Item, related_name='ordered_items', on_delete=models.CASCADE)
    client = models.ForeignKey(Client, related_name='client_ordered_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.IntegerField(default=1, choices=ORDER_STATUS)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.item.name} - {self.quantity}"
    

    def total_price(self):
        item_price = self.item.price
        return item_price * self.quantity
        

