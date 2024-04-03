from django.urls import path
from . import views

# Define URL patterns
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('welcome/', views.welcome, name='welcome'),
]


