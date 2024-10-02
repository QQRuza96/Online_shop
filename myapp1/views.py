from django.shortcuts import render
from myapp1.models import Product

def index_page(request):
    all_product = Product.objects.all()
    message = None

    if request.method == 'GET' and request.GET:
        for key, value in request.GET.items():
            if key.startswith('name_') and value:
                product_name = key.split('_')[1]
                quantity_to_add = int(value)

                try:
                    product = Product.objects.get(name=product_name)

                    cart_product = request.session.get('cart', {})

                    current_quantity_in_cart = cart_product.get(product_name, {}).get('quantity', 0)

                    total_quantity = current_quantity_in_cart + quantity_to_add

                    if total_quantity > product.quantity:
                        message = f"Не хватает товаров на складе. Доступно только {product.quantity}."
                    else:
                        if product_name in cart_product:
                            cart_product[product_name]['quantity'] = total_quantity
                        else:
                            # Добавляем цену здесь
                            cart_product[product_name] = {
                                'id': product.id,
                                'quantity': total_quantity,
                                'price': product.price  # Сохраняем цену продукта
                            }
                        
                        request.session['cart'] = cart_product
                        print(f'Корзина обновлена: {request.session["cart"]}')

                except Product.DoesNotExist:
                    message = f"Продукт с именем {product_name} не найден."

    return render(request, 'index.html', context={'data': all_product, 'message': message})

def cart_page(request):
    cart_product = request.session.get('cart', {})

    # Очищение корзины
    if request.method == 'GET' and 'action' in request.GET:
        if request.GET['action'] == 'resets':
            request.session['cart'] = {}
            print("Корзина очищена")
            cart_product = {}

    # Формируем данные для шаблона
    cart_items = []
    total_total = 0.0
    for product_name, details in cart_product.items():
        try:
            product = Product.objects.get(id=details['id'])  # Получаем продукт по ID
            total_price = details['quantity'] * details['price']  # Расчет общей цены
            cart_items.append({
                'product': product,
                'quantity': details['quantity'],
                'price': details['price'],
                'total_price': total_price  # Общая цена
            })
            
            total_total += total_price
                
        except Product.DoesNotExist:
            continue

    return render(request, 'cart.html', context={'data': cart_items, 'total_total': total_total})
