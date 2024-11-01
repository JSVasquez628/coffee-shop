from .views import ProductFormView, ProductListAPI, ProductListView
from django.urls import path

urlpatterns = [
    path('', ProductListView.as_view(), name="list_products"),
    path('api/', ProductListAPI.as_view(), name="list_products_api"),
    path('agregar/', ProductFormView.as_view(), name="add_products"),
    path('api/<int:pk>', ProductListAPI.as_view(), name="list_products_api_1")
]
    