from django.urls import path
from . import models

# Define URL patterns
urlpatterns = [
    path('login/', models.user_login, name='login'),
    path('welcome/', models.welcome, name='welcome'),
    path('logout/', models.user_logout, name='logout'),
]


