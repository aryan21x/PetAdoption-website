from django.urls import path
from . import views

urlpatterns = [
    path('worker_page/', views.worker_page, name='worker_page'),
    path('delete_worker/<int:worker_id>/', views.delete_worker, name='delete_worker'),
    path('sort_worker/', views.sort_worker, name='sort_worker'),
    path('edit_worker/<int:worker_id>/', views.edit_worker, name='edit_worker')
]