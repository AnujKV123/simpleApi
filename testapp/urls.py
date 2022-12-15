from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.Products, name="products"),
    path('products/<int:id>', views.getProduct, name="getProduct")
]
