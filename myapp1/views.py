from urllib import response
from .models import Type, Item
from django.shortcuts import render 
from django.shortcuts import get_object_or_404
# Create your views here.


def index(request):
    type_list = Type.objects.all().order_by('id')[:7]
    # b - iii) extra variables are passed to the template
    # variable name - type_list
    return render(request, 'myapp1/index0.html', {'type_list': type_list})
    


def about(request):
    # d- iii) extra variables are not passed to the template
    return render(request, 'myapp1/about0.html')


def detail(request, type_no):
    type_obj = get_object_or_404(Type, pk=type_no)
    item_list = Item.objects.filter(type=type_obj)
    # e -iv) extra variables are passed to the template
    # e - v) variable name - item_list
    return render(request, 'myapp1/detail0.html', {'item_list': item_list})