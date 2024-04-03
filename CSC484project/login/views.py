
from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponseRedirect
import mysql.connector

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="rootnew",
    password="1234",
    database="project" 
)

def login(request):
    return render(request, 'loginView.html')

class HomeView(TemplateView):
    template_name = 'homeView.html'

    # Define login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user against MySQL database
        cursor = mydb.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_table WHERE username = %s AND password = %s", (username, password))
        user_row = cursor.fetchone()

        if user_row:
            # Create Django user object
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page or home page
                return HttpResponseRedirect('/success/')
        else:
            # Invalid login
            return render(request, 'loginView.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'loginView.html')

