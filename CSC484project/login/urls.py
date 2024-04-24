from django.urls import path
from . import views
# Define URL patterns
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('welcome/', views.welcome, name='welcome'),
    path('logout/', views.user_logout, name='logout'),
]


