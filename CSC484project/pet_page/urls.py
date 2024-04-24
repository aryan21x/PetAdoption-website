from django.urls import path
from . import views

urlpatterns = [
    path('pet_page/', views.pet_page, name='pet_page'),
    path('delete_pet/<int:pet_id>/', views.delete_pet, name='delete_pet'),
]