from django.urls import path
from .views import (
    Homepage, Wishlist, Cart,
    ProductDetail, SignUp, SignIn,
    Checkout, About, Contact, Index,
    CartN, CheckoutN, Shop, ShopDetail
)

app_name = 'web'

urlpatterns = [
    path('', Homepage.as_view(), name='home'),
    path('wishlist/', Wishlist.as_view(), name='wishlist'),
    path('cart/', Cart.as_view(), name='cart'),
    path('product-detail/<int:product_id>/',
         ProductDetail.as_view(), name='product-detail'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('signin/', SignIn.as_view(), name='signin'),
    path('checkout/', Checkout.as_view(), name='checkout'),
    path('about/', About.as_view(), name='about'),
    path('contact/', Contact.as_view(), name='contact'),
    path('index/', Index.as_view(), name='index'),
    path('cartn/', CartN.as_view(), name='cartn'),
    path('checkoutn/', CheckoutN.as_view(), name='checkoutn'),
    path('shop/', Shop.as_view(), name='shop'),
    path('<int:item_id>/', ShopDetail.as_view(), name='shop-detail'),
]
