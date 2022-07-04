from django.shortcuts import render, redirect
from .models import Supplier, Product, Distributor, Location
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

#PRODUCTS
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

def deleteproduct(request, id):
    Product.objects.get(id = id).delete()
    return redirect(productlistview)

def confirmdeleteproduct(request, id):
    product = Product.objects.get(id = id)
    context = {'product': product}
    return render (request,"confirmdeleteproduct.html",context)   

#SUPPLIERS
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

def editsupplierget(request, id):
    supplier = Supplier.objects.get(id = id)
    context = {'supplier': supplier}
    return render (request,"editsupplier.html",context)

def editsupplierpost(request, id):
    item = Supplier.objects.get(id = id)
    item.companyname = request.POST['companyname']
    item.contactname = request.POST['contactname']
    item.address = request.POST['address']
    item.phone = request.POST['phone']
    item.email = request.POST['email']
    item.country = request.POST['country']
    item.save()
    return redirect(supplierlistview)        

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

#DISTRIBUTORS
def distributorlistview(request):
    distributorlist = Distributor.objects.all()
    context ={'distributors': distributorlist}
    return render(request, 'distributorlist.html', context)

def adddistributor(request):
    a = request.POST['companyname']
    b = request.POST['contactname']
    c = request.POST['address']
    d = request.POST['phone']
    e = request.POST['email']
    f = request.POST['country']
    Distributor(companyname = a, contactname = b, address = c, phone = d, email = e, country = f).save()
    return redirect(request.META['HTTP_REFERER'])

def editdistributorget(request, id):
    distributor = Distributor.objects.get(id = id)
    context = {'distributor': distributor}
    return render (request,"editdistributor.html",context)

def editdistributorpost(request, id):
    item = Distributor.objects.get(id = id)
    item.companyname = request.POST['companyname']
    item.contactname = request.POST['contactname']
    item.address = request.POST['address']
    item.phone = request.POST['phone']
    item.email = request.POST['email']
    item.country = request.POST['country']
    item.save()
    return redirect(distributorlistview)   

def deletedistributor(request, id):
    Distributor.objects.get(id = id).delete()
    return redirect(distributorlistview)

def confirmdeletedistributor(request, id):
    distributor = Distributor.objects.get(id = id)
    context = {'distributor': distributor}
    return render (request,"confirmdeletedistributor.html",context)    

def searchdistributors(request):
    search = request.POST['search']
    filtered = Distributor.objects.filter(companyname__icontains=search)
    context = {'distributors': filtered}
    return render (request,"searchdistributors.html",context)

#LOCATIONS
def locationlistview(request):
    locationlist = Location.objects.all()
    context ={'locations': locationlist}
    return render(request, 'locationlist.html', context)

def addlocation(request):
    a = request.POST['name']
    b = request.POST['address']
    c = request.POST['postalcode']
    Location(name = a, address = b, postalcode = c).save()
    return redirect(request.META['HTTP_REFERER'])

def editlocationget(request, id):
    location = Location.objects.get(id = id)
    context = {'location': location}
    return render (request,"editlocation.html",context)

def editlocationpost(request, id):
    item = Location.objects.get(id = id)
    item.name = request.POST['name']
    item.address = request.POST['address']
    item.postalcode = request.POST['postalcode']
    item.save()
    return redirect(locationlistview)   

def deletelocation(request, id):
    Location.objects.get(id = id).delete()
    return redirect(locationlistview)

def confirmdeletelocation(request, id):
    location = Location.objects.get(id = id)
    context = {'location': location}
    return render (request,"confirmdeletelocation.html",context)    

def searchlocations(request):
    search = request.POST['search']
    filtered = Location.objects.filter(companyname__icontains=search)
    context = {'locations': filtered}
    return render (request,"searchlocations.html",context)    