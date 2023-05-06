from products.models import Products


class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get['cart']
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add_to_cart(self, product, quantity=1):
        """
        add a specific product with quantity of it in the cart.
        """
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart['product_id'] = {
                'quantity': quantity,
            }
        else:
            self.cart['product_id']['quantity'] += quantity
        self.save_to_cart()

    def remove_from_cart(self, product):
        """
        remove specific product from the cart.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save_to_cart()

    def __iter__(self):
        """
        get and iteration every object of a product who added in cart from database.
        """
        product_ids = self.cart.keys()
        products = Products.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product_objects'] = product
        for value in cart.values():
            yield value

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
        return len(self.cart.keys())

