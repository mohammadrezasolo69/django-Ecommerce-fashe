from ecommerce_product.models import StoreProducts
from decimal import Decimal

NAME_SESSION = 'cart'


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(NAME_SESSION)
        if not cart:
            cart = self.session[NAME_SESSION] = {}
        self.cart = cart

    def __iter__(self):
        product_ids = self.cart.keys()
        products = StoreProducts.objects.filter(id__in=product_ids)
        copy_cart = self.cart.copy()

        for product in products:
            copy_cart[str(product.id)]['product'] = product

        for total in copy_cart.values():
            total['total_price'] = Decimal(total['price']) * total['quantity']
            yield total

    def add(self, product, quantity):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'price': product.price, 'quantity': 0}
        self.cart[product_id]['quantity'] += quantity
        self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session.modified = True

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
