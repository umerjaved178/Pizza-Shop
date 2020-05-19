from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cart/", views.cart, name="cart"),
    path("cart/delete/<str:id>",views.deletecartitem,name='delete'),
    path("add/",views.additem,name='additem'),
    path("login", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("place_order", views.place_order, name="place_order"),
    path("orders_page", views.orders_page, name="orders_page"),
    path("userhistory", views.userhistory, name="history"),
    path("status_url/<str:id>", views.changestatus, name="status_url"),
    
]