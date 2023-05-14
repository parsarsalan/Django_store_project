from products.models import Products


class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add_to_cart(self, product, quantity=1, replace_current_quantity=False):
        """
        add a specific product with quantity of it in the cart.
        """
        pk = str(product.id)

        if pk not in self.cart:
            self.cart[pk] = {'quantity': 0}

        if replace_current_quantity:
            self.cart[pk]['quantity'] = quantity
        else:
            self.cart[pk]['quantity'] += quantity
        self.save_to_cart()

    def remove_from_cart(self, product):
        """
        remove specific product from the cart.
        """
        pk = str(product.id)
        if pk in self.cart:
            del self.cart[pk]
            self.save_to_cart()

    def __iter__(self):
        """
        get and iteration on every object of a product who added in cart from database.
        """
        product_ids = self.cart.keys()
        products = Products.objects.filter(id__in=product_ids)

        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product_obj'] = product

        for item in cart.values():
            item['total_price'] = item['quantity'] * item['product_obj'].price
            yield item

    def save_to_cart(self):
        """
        it is saving changes to in session.
        """
        self.session.modified = True

    def clear_all(self):
        """
        clear all the products in the cart.
        """
        del self.session['cart']
        self.save_to_cart()

    def __len__(self):
        """
        get a len of all products already added in cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def total_price(self):
        """
        get total price of products in cart.
        """
        products_ids = self.cart.keys()
        return sum(item['quantity']*item['product_obj'].price for item in self.cart.values())
