from django.urls import path

from .views import loginview, login_action, logout_action
from .views import supplierlistview, addsupplier, confirmdeletesupplier, deletesupplier, editsupplierget, editsupplierpost, searchsuppliers
from .views import productlistview, addproduct, productsfiltered, editproductget, editproductpost
from .views import distributorlistview, adddistributor, confirmdeletedistributor, deletedistributor, searchdistributors, editdistributorget, editdistributorpost

urlpatterns = [
    
    # Login & logout
    path('', loginview),
    path('login/', login_action),
    path('logout/', logout_action),

    # Products url´s
    path('products/', productlistview),
    path('add-product/', addproduct),
    path('products-by-supplier/<int:id>/', productsfiltered),
    path('edit-product-get/<int:id>/', editproductget),
    path('edit-product-post/<int:id>/', editproductpost), 

    # Supplier url´s
    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),
    path('edit-supplier-get/<int:id>/', editsupplierget),
    path('edit-supplier-post/<int:id>/', editsupplierpost), 
    path('delete-supplier/<int:id>/', deletesupplier),
    path('confirm-delete-supplier/<int:id>/', confirmdeletesupplier),
    path('search-suppliers/', searchsuppliers),

    # Distributor url´s
    path('distributors/', distributorlistview),
    path('add-distributor/', adddistributor),
    path('edit-distributor-get/<int:id>/', editdistributorget),
    path('edit-distributor-post/<int:id>/', editdistributorpost), 
    path('delete-distributor/<int:id>/', deletedistributor),
    path('confirm-delete-distributor/<int:id>/', confirmdeletedistributor),
    path('search-distributors/', searchdistributors),
]