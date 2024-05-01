from django.urls import path
from . import views
# Define URL patterns
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('welcome/', views.welcome, name='welcome'),
    path('logout/', views.user_logout, name='logout'),
    path('register/',views.register,name='register'),
    path('error_page/',views.error_page,name='error_page'),
    path('not_found/',views.not_found, name='not_found'),
]


