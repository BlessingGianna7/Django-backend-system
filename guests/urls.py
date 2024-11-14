from django.urls import path
from .views import guest_list, add_guest, edit_guest, delete_guest

urlpatterns = [
    path('', guest_list, name='guest_list'),
    path('add/', add_guest, name='add_guest'),
    path('edit/<int:guest_id>/', edit_guest, name='edit_guest'),
    path('delete/<int:guest_id>/', delete_guest, name='delete_guest'),
]