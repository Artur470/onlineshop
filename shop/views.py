from django.shortcuts import render, get_object_or_404
from .models import Category, Product
def product_list(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    # Фильтруем по категории, если category_slug предоставлен
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    else:
        category = None  # если категории нет, установим значение None

    # Получаем просмотренные продукты из сессии
    viewed_products_ids = request.session.get('viewed_products', [])
    viewed_products = Product.objects.filter(id__in=viewed_products_ids)

    return render(request, 'shop/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products,
        'viewed_products': viewed_products,
    })

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)

    # Инициализируем список просмотренных продуктов, если он отсутствует
    viewed_products = request.session.get('viewed_products', [])

    # Добавляем текущий продукт в список просмотренных, если его там нет
    if id not in viewed_products:
        viewed_products.append(id)

    # Ограничиваем количество просмотренных продуктов до 10
    if len(viewed_products) > 10:
        viewed_products.pop(0)

    # Обновляем сессию
    request.session['viewed_products'] = viewed_products

    return render(request, 'shop/product/detail.html', {
        'product': product
    })