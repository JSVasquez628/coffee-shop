from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Orden

class MyOrderView(LoginRequiredMixin, DetailView):
    model = Orden
    template_name = 'orders/my_orders.html'
    context_object_name = "order"
    
    def get_object(self, queryset=None):
        return Orden.objects.filter(is_active=True, user=self.request.user).first
