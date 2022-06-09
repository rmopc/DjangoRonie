from django.shortcuts import render, redirect
from .models import Supplier, Product
from django.contrib.auth import authenticate, login, logout

def loginview(request):
    return render (request, "loginpage.html")

def login_action(request):
    user = request.POST['username']
    passw = request.POST['password']
    # Löytyykö kyseistä käyttäjää?
    user = authenticate(username = user, password = passw)
    #Jos löytyy:
    if user:
        # Kirjataan sisään
        login(request, user)
        # Tervehdystä varten context
        context = {'name': user.first_name}
        # Kutsutaan suoraan landingview.html
        return render(request,'landingpage.html',context)
    # Jos ei kyseistä käyttäjää löydy
    else:
        return render(request, 'loginerror.html')    

def logout_action(request):
    logout(request)
    return render(request, 'loginpage.html')

def productlistview(request): #Tämän voi kopioida muihin funktioihin, johon halutaan auth.
    if not request.user.is_authenticated:
        return render(request, 'loginpage.html')
    else:
        productlist = Product.objects.all()
        supplierlist = Supplier.objects.all()
        context = {'products': productlist, 'suppliers': supplierlist}
        return render (request,"productlist.html",context)

def addproduct(request):
    a = request.POST['productname']
    b = request.POST['packagesize']
    c = request.POST['unitprice']
    d = request.POST['unitsinstock']
    e = request.POST['supplier']
    
    Product(productname = a, packagesize = b, unitprice = c, unitsinstock = d, supplier = Supplier.objects.get(id = e)).save()
    return redirect(request.META['HTTP_REFERER'])    

def productsfiltered(request, id):
    productlist = Product.objects.all()
    supplierlist = Supplier.objects.all()
    supplier = Supplier.objects.get(id = id)
    filteredproducts = productlist.filter(supplier = id)
    context ={'products': filteredproducts, 'suppliers': supplierlist, "supplier" : supplier}
    return render (request,"filteredproductlist.html",context)    

def editproductget(request, id):
    product = Product.objects.get(id = id)
    context = {'product': product}
    return render (request,"editproduct.html",context)


def editproductpost(request, id):
    item = Product.objects.get(id = id)
    item.unitprice = request.POST['unitprice']
    item.unitsinstock = request.POST['unitsinstock']
    item.save()
    return redirect(productlistview)    

def supplierlistview(request):
    supplierlist = Supplier.objects.all()
    context ={'suppliers': supplierlist}
    return render(request, 'supplierlist.html', context)

def addsupplier(request):
    a = request.POST['companyname']
    b = request.POST['contactname']
    c = request.POST['address']
    d = request.POST['phone']
    e = request.POST['email']
    f = request.POST['country']
    Supplier(companyname = a, contactname = b, address = c, phone = d, email = e, country = f).save()
    return redirect(request.META['HTTP_REFERER'])

def deletesupplier(request, id):
    Supplier.objects.get(id = id).delete()
    return redirect(supplierlistview)

def confirmdeletesupplier(request, id):
    supplier = Supplier.objects.get(id = id)
    context = {'supplier': supplier}
    return render (request,"confirmdeletesupplier.html",context)    

def searchsuppliers(request):
    search = request.POST['search']
    filtered = Supplier.objects.filter(companyname__icontains=search)
    context = {'suppliers': filtered}
    return render (request,"searchsuppliers.html",context)