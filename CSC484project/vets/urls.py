from django.urls import path
from . import views

urlpatterns = [
    path('vet_page/', views.vet_page, name='vet_page'),
    path('delete_vet/<int:vet_id>/', views.delete_vet, name='delete_vet'),
    path('edit_vet/<int:vet_id>/', views.edit_vet, name='edit_vet'),
    path('sort_vet/', views.sort_vet, name='sort_vet'),
]