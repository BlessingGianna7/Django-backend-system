from django.urls import path
from .views import animal_list, add_animals, edit_animal, delete_animal

urlpatterns = [
    path('', animal_list, name='animal_list'),
    path('add/', add_animals, name='add_animals'),
    path('edit/<int:animal_id>/', edit_animal, name='edit_animal'),
    path('delete/<int:animal_id>/', delete_animal, name='delete_animal'),
]