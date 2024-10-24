from .views import ProductFormView, ProductListView
from django.urls import path

urlpatterns = [
    path('', ProductListView.as_view(), name="list_products"),
    path('agregar/', ProductFormView.as_view(), name="add_products"),
]
    