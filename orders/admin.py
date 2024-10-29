from django.contrib import admin
from .models import Orden, OrderProduct

class OrderProductInlineAdmin(admin.TabularInline):
    model = OrderProduct
    extra = 0

class OrdenAdmin(admin.ModelAdmin):
    model = Orden
    inlines = [
        OrderProductInlineAdmin
    ]
    
admin.site.register(Orden, OrdenAdmin)
