from django.contrib import admin
from django.urls import path
from store import views
from store.controller import authview, cart, checkout, order

urlpatterns = [
    path('', views.home, name="home"),
    path('collections', views.collections, name="collections"),
    path('collections/<str:slug>', views.collectionsview, name="collectionsview"),
    path('collections/<str:cate_slug>/<str:prod_slug>', views.productview, name="productview"),

    path('register/', authview.register, name="register"),
    path('login/', authview.loginpage, name="loginpage"),
    path('logout/', authview.logoutpage, name="logout"),

    path('add-to-cart', cart.addtocart, name="addtocart"),
    path('cart', views.viewcart, name="cart"),
    path('update-cart', cart.updatecart, name="updatecart"),
    path('delete-cart-item', cart.deletecartitem, name="deletecartitem"),
    path('checkout', checkout.index, name="checkout"),
    path('place-order', checkout.placeorder, name="placeorder"),

    path('proceed-to-pay', checkout.razorpaycheck),

    path('my-orders', order.index, name="myorders"),

    path('view-order/<str:t_no>', order.vieworder, name="orderview"),
]