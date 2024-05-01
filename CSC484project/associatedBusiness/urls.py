from django.urls import path
from . import views


urlpatterns = [
    path('business_page/', views.business_page, name='business_page'),
    path('delete_business/<int:business_id>/', views.delete_business, name='delete_business'),
    path('sort_business/', views.sort_business, name='sort_business'),
    path('edit_business/<int:business_id>/', views.edit_business, name='edit_business')
]