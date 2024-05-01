from django.urls import path
from . import views

urlpatterns = [
    path('pet_page/', views.pet_page, name='pet_page'),
    path('delete_pet/<int:pet_id>/', views.delete_pet, name='delete_pet'),
    path('sort_pet/', views.sort_pet, name='sort_pet'),
    path('edit_pet/<int:pet_id>/', views.edit_pet, name='edit_pet'),
    path('homePet/<int:pet_id>/', views.homePet, name='homePet'),
]