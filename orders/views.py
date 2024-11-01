from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Orden
from .forms import OrderProductForm

class MyOrderView(LoginRequiredMixin, DetailView):
    model = Orden
    template_name = 'orders/my_orders.html'
    context_object_name = "order"
    
    def get_object(self, queryset=None):
        return Orden.objects.filter(is_active=True, user=self.request.user).first()
    
class CreateOrderProductView(LoginRequiredMixin, CreateView):
    template_name = 'orders/create_order_product.html'
    form_class = OrderProductForm
    success_url = reverse_lazy('mi-orden')
    
    def form_valid(self, form):
        order, _ = Orden.objects.get_or_create(
            is_active = True,
            user = self.request.user,
        )
        form.instance.order = order
        form.instance.quantity = 1
        form.save()
        return super().form_valid(form)
