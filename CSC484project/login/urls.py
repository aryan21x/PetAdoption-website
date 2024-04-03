from django.urls import path
from . import views
import mysql.connector

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="rootnew",
    password="1234",
    database="project" 
)

# Define URL patterns
urlpatterns = [
    path('login/', views.login_view, name='login'),
]


