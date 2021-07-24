from django.contrib import admin
from django.urls import path
from .views import home, signup, login , cart, searched_product
from .views.login import logout
from .views.checkout import CheckOut
from .views.orders import OrderView
from .views.aboutus import AboutUs
from .views.emergency import Emergency
from store.middlewares.auth import auth_middleware


urlpatterns = [
    path('', home.Index.as_view(), name='homepage'),
    path('signup', signup.Signup.as_view(), name='signup_page'),
    path('login', login.Login.as_view(), name='login_page'),
    path('logout', logout, name='logout_page'),
    path('cart', cart.Cart.as_view(), name='cart_page'),
    path('check-out', auth_middleware(CheckOut.as_view()), name='checkout_page'),
    path('orders', OrderView.as_view(), name='orders_page'),
    path('emergency', Emergency.as_view()),
    path('aboutus', AboutUs.as_view()),
    path('searched-product', searched_product.searched_products, name='searched_products_page')
]
