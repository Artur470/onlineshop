# shop/urls.py

from django.urls import path
from .views import product_list, product_detail

app_name = 'shop'

urlpatterns = [
    path('list/', product_list, name='product_list'),  # Путь для отображения всех продуктов
    path('categories/<slug:category_slug>/', product_list, name='product_list_by_category'),  # Новый путь для фильтрации по категории
    path('detail/<int:id>/<slug:slug>/', product_detail, name='product_detail'),  # Путь для детального просмотра продукта
]
