from django.urls import path
from .views import Home, OrderCart, PizzaCart, ToppingCart

urlpatterns = [
    path('', Home.as_view()),
    path('api/pizza/bases/', PizzaCart.as_view()),
    path('api/pizza/toppings/', ToppingCart.as_view()),
    path('api/orders/', OrderCart.as_view()),
    path('api/orders/<int:order_id>', OrderCart.as_view()),
]
