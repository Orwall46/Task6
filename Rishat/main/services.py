"""Some utils for views"""
def convertor_price(item):
    """Convert currency for Order Cart to USD"""
    amd = 411
    rub = 64
    eur = 0.98
    try:
        if item.currency == "AMD":
            item.price = item.price / amd
        elif item.currency == "RUB":
            item.price = item.price / rub
        elif item.currency == "EUR":
            item.price = item.price / eur
        elif item.currency == "USD":
            return item.price
    except Exception as ex:
        print(ex)
    return round(item.price, 2)


def order_summ(orders):
    order_sum = 0
    for order in orders:
        order_sum += round(convertor_price(order.item), 2)
    return order_sum


def list_items(orders):
    items = []
    for order in orders:
        items.append(
            {
            'price_data': {
                'currency': 'usd',
                'product_data': {
                'name': order.item.name,
                },
                'unit_amount': int((order.item.price) * 100),
            },
            'quantity': 1,
            }
        )
    return items
