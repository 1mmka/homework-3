from django.contrib import admin
from django.urls import path
from app.views import ProductsList,deleteProduct

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',ProductsList.as_view(),name='list-products'),
    path('del-product/<int:pk>',deleteProduct,name='del-product')
]
