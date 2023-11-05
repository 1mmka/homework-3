from typing import Any
from django import http
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.views.generic import ListView
from app.models import Product
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.views.decorators.cache import cache_control


#server-cache-test
CACHE_TTL = 30
# class ProductsList(ListView):
#     model = Product
#     context_object_name = 'products'
#     template_name = 'index.html'
    
#     @method_decorator(cache_page(CACHE_TTL))
#     def dispatch(self, request: http.HttpRequest, *args: Any, **kwargs: Any) -> http.HttpResponse:
#         return super().dispatch(request, *args, **kwargs)
    
#     def get_queryset(self) -> QuerySet[Any]:
#         cached_data = cache.get('products')
#         if cached_data is None:
#             products = Product.objects.all()
#             cache.set('products', products, CACHE_TTL)
#             cached_data = products
#         return cached_data


#user-cache-test
class ProductsList(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'index.html'

    @method_decorator(cache_control(max_age=30))
    def dispatch(self, request: http.HttpRequest, *args: Any, **kwargs: Any) -> http.HttpResponse:
        return super().dispatch(request, *args, **kwargs)
    
    def get_queryset(self) -> QuerySet[Any]:
        cached_data = cache.get('products')
        if cached_data is None:
            products = Product.objects.all()
            cache.set('products', products, CACHE_TTL)
            cached_data = products
        return cached_data
    

def deleteProduct(request,pk):
    product = Product.objects.get(pk = pk)
    product.delete()
    
    return redirect('list-products')