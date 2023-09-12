from django.urls import path, include
from raffinato.accounts.views import login, register, profile_details, profile_edit, profile_delete

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/<int:pk>/', include([
        path('', profile_details, name='profile_details'),
        path('edit/', profile_edit, name='profile_edit'),
        path('delete/', profile_delete, name='profile_delete')
    ]))
]
