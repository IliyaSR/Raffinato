from django.urls import path, include
from raffinato.common.views import home, about

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
]
