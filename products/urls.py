from .views import ProductFormView
from django.urls import path

urlpatterns = [
    path('agregar/', ProductFormView.as_view(), name="add_products"),
]
