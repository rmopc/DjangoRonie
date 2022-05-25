from django.shortcuts import render
from .models import Supplier, Product

def landingview(request):
    return render(request, 'landingpage.html')

def productlistview(request):
    productlist = Product.objects.all()
    context ={'products': productlist}
    return render(request, 'productlist.html', context)

def supplierlistview(request):
    supplierlist = Supplier.objects.all()
    context ={'suppliers': supplierlist}
    return render(request, 'supplierlist.html', context)