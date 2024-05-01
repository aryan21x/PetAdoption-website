"""
URL configuration for CSC484project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# urls.py
from django.contrib import admin
from django.urls import path, include
from login.views import home  # Import the view for the home page

urlpatterns = [
    path('', home , name='home'),  # URL pattern for the home page
    path('admin/', admin.site.urls),
    path('', include('login.urls')),  # URL pattern for 'login' app
    path('', include('pet_page.urls')), # URL pattern for 'pets' app
    path('', include('shelters.urls')), # URL pattern for 'shetters' app
    path('', include('workers.urls')), # URL pattern for 'workers' app
    path('', include('adopters.urls')), # URL pattern for 'adopters' app
    path('', include('vets.urls')), # URL pattern for 'vets' app
    path('', include('associatedBusiness.urls')), # URL pattern for 'business' app
]
