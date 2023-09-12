from django.urls import path, include
from raffinato.shoes.views import all_shoes, add_shoes, view_shoes

urlpatterns = [
    path('', all_shoes, name='all_shoes'),
    path('add/', add_shoes, name='add_shoes'),
    path('shoes/<int:pk>/<slug:shoe_slug>/', include([
        path('', view_shoes, name='details_shoes'),
    ]))

]