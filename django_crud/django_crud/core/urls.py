
from unicodedata import name
from django.urls import re_path, path
from .views import list_products


urlpatterns = [
    path('', list_products, name='list_projects'),
    path('new_product', create_products, name='create_products')

]