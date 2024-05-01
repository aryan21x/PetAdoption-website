from django.views.generic import TemplateView
from django.shortcuts import render ,redirect
import mysql.connector
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .backends import MySQLBackend

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="rootnew",
    password="1234",
    database="project" 
)

def error_page(request):
    return render(request, 'error_page.html')

def not_found(request):
    return render(request, 'not_found.html')

def welcome(request):
    return render(request, 'welcome.html')


def home(request):
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pets")
    pets = cursor.fetchall()
    return render(request, 'homeView.html', {'pets': pets})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user against MySQL database
        user = MySQLBackend().authenticate(request, username=username, password=password)
        
        if user is not None:
            # Login the user
            login(request, user)
            return render(request, 'homeView.html')
        else:
            # Invalid login
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    
    # GET request or invalid form submission
    return render(request, 'login.html')

@login_required
def user_logout(request):
    logout(request)
    return render(request, 'logout.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            cursor = mydb.cursor()
            cursor.execute("INSERT INTO user_table (username, password) VALUES (%s, %s)", (name, password1))
            mydb.commit()
            return redirect('login')
        else:
            return render(request, 'register.html', {'error_message': 'password does nott match'})

    return render(request,'register.html')