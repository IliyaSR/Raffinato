from django.urls import path, include
from raffinato.suits.views import shop_list, add_suit, edit_suit, details_suit

urlpatterns = [
    path('', shop_list, name='shop_list'),
    path('add/', add_suit, name='add_suit'),
    path('suit/<int:pk>/<slug:suit_slug>/', include([
        path('', details_suit, name='details_suit'),
        path('edit/', edit_suit, name='edit_suit')
    ]))

]
