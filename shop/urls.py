from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Index"),
    path('about/', views.about, name="AboutUs"),
    path('contact/', views.contact, name="Contact Us"),
    path('search/', views.search, name="Search"),
    path('products/<int:myid>', views.productview, name="productview"),
    path('checkout/', views.checkout, name="Checkout"),
    path('tracker/', views.tracker, name="Tracker"),
]