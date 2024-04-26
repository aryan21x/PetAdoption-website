from django.urls import path
from . import views

urlpatterns = [
    path('shelter_page/', views.shelter_page, name='shelter_page'),
    path('delete_shelter/<int:shelter_id>/', views.delete_shelter, name='delete_shelter'),
    path('edit_shelter/<int:shelter_id>/', views.edit_shelter, name='edit_shelter'),
    path('sort_shelter/', views.sort_shelter, name='sort_shelter'),
]