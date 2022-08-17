
from unicodedata import name
from django.urls import re_path, path
from .views import list_products, create_products, update_products, delete_products


urlpatterns = [
    path('', list_products, name='list_products'),
    path('new_product', create_products, name='create_products'),
    path('update/<int:id>/', update_products, name='update_products'),
    path('delete/<int:id>/', delete_products, name='delete_products')

]