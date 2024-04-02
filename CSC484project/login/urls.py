from django.urls import path
from . import views
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
import mysql.connector

urlpatterns = [
    path('', views.login, name='login'),
]


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or home page
            return HttpResponseRedirect('/success/')
        else:
            # Invalid login
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'login.html')

def connect_to_mysql():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="yourusername",
            password="yourpassword"
        )
        print("MySQL connection successful.")
        return mydb
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None

# Call the function to establish a connection
mydb = connect_to_mysql()

