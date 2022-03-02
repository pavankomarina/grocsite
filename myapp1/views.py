from urllib import response
from django.http import HttpResponse
from .models import Type, Item
from django.shortcuts import get_object_or_404
# Create your views here.


def index(request):
    item_list = Item.objects.all().order_by('-price')[:7]
    response = HttpResponse()
    heading1 = '<p>' + 'Top 7 Items: ' + '</p>'
    response.write(heading1)
    para = ''
    for item in item_list:
        para += '<p>'+ str(item.id) + ': ' + str(item) + '</p>'
    response.write(para)
    return response


def about(request):
    return HttpResponse('<h1>This is an Online Grocery Store</h1>')


def detail(request, type_no):
    type_obj = get_object_or_404(Type, pk=type_no)
    item_list = Item.objects.filter(type=type_obj)
    response = HttpResponse()
    heading1 = '<p>' + f"Items for type " + '</p>'
    response.write(heading1)
    para = ''
    for item in item_list:
        para += '<p>'+ str(item.id) + ': ' + str(item) + '</p>'
    response.write(para)

    return response