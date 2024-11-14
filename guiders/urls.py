from django.urls import path
from . import views

urlpatterns = [
    path('', views.guider_list, name='guider_list'),
    path('add/', views.add_guider, name='add_guider'),
    path('edit/<int:guider_id>/', views.edit_guider, name='edit_guider'),  # Make sure this matches your template
    path('delete/<int:guider_id>/', views.delete_guider, name='delete_guider'),
]