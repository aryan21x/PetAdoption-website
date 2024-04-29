from django.urls import path
from . import views

urlpatterns = [
    path('adopter_page/', views.adopter_page, name='adopter_page'),
    path('delete_adopter/<int:adopt_id>/', views.delete_adopter, name='delete_adopter'),
    path('edit_adopter/<int:adopt_id>/', views.edit_adopter, name='edit_adopter'),
    path('sort_adopter/', views.sort_adopter, name='sort_adopter'),
]