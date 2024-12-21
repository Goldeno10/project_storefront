from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
import json


class Homepage(TemplateView):
    template_name = 'web/homepage.html'

    def get_context_data(self, **kwargs: Any) -> dict:
        products = [
            {
                "name": "Product 1",
                        "price": 20.99,
                        "stock": 50
            },
            {
                "name": "Product 2",
                        "price": 34.99,
                        "stock": 30
            },
            {
                "name": "Product 3",
                        "price": 15.49,
                        "stock": 70
            }

        ]

        context = super().get_context_data(**kwargs)
        context['title'] = 'Homepage'
        context['products'] = products

        return context


class Wishlist(TemplateView):
    """ Wishlist View """
    template_name = "web/wishlist.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        wishlist = [
            {
                "name": "Beautiful Card",
                "price": 100,
                "oldPrice": 90
            },
            {
                "name": "Elegant Notebook",
                "price": 25,
                "oldPrice": 20
            },
            {
                "name": "Stylish Pen Set",
                "price": 15,
                "oldPrice": 12
            },
            {
                "name": "Fancy Pencil",
                "price": 5,
                "oldPrice": 4
            },
            {
                "name": "Cute Eraser",
                "price": 2,
                "oldPrice": 1
            },

        ]

        wishlist_lenght = len(wishlist)
        context = super().get_context_data(**kwargs)
        context['wishlist'] = wishlist
        context['wishlist_lenght'] = wishlist_lenght

        return context


class Cart(TemplateView):
    """ Cart View """
    template_name = "web/cart.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        cart = [
            {
                "name": "Beautiful Card",
                "price": 100,
                "oldPrice": 90
            },
            {
                "name": "Elegant Notebook",
                "price": 25,
                "oldPrice": 20
            },
            {
                "name": "Stylish Pen Set",
                "price": 15,
                "oldPrice": 12
            },
            {
                "name": "Fancy Pencil",
                "price": 5,
                "oldPrice": 4
            },
            {
                "name": "Cute Eraser",
                "price": 2,
                "oldPrice": 1
            },

        ]
        products = [
            {
                "name": "Product 1",
                "price": 20.99,
                "stock": 50
            },
            {
                "name": "Product 2",
                "price": 34.99,
                "stock": 30
            },
            {
                "name": "Product 3",
                "price": 15.49,
                "stock": 70
            }

        ]

        total = 2455
        cart_lenght = len(cart)
        context = super().get_context_data(**kwargs)
        context['cart'] = cart
        context['total'] = total
        context['cart_lenght'] = cart_lenght
        context['products'] = products

        return context


class ProductDetail(TemplateView):
    """ Product Detail View """
    template_name = "web/product_detail.html"


class SignUp(TemplateView):
    """ Sign Up View """
    template_name = "web/signup.html"


class SignIn(TemplateView):
    """ Sign In View """
    template_name = "web/signin.html"


class Checkout(TemplateView):
    """ Checkout View """
    template_name = "web/checkout.html"


class About(TemplateView):
    """ About View """
    template_name = "web/about.html"


class Contact(TemplateView):
    """ Contact View """
    template_name = "web/contact.html"


class Index(TemplateView):
    template_name = 'web/temp/index.html'


class CartN(TemplateView):
    template_name = 'web/temp/cart.html'


class CheckoutN(TemplateView):
    template_name = 'web/temp/checkout.html'


class Shop(TemplateView):
    template_name = 'web/temp/shop.html'


class ShopDetail(TemplateView):
    template_name = 'web/temp/shop-detail.html'


