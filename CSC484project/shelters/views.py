from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Shelter
import mysql.connector
from django.conf import settings
from django.shortcuts import redirect

mydb = mysql.connector.connect(
            host=settings.DB_HOST,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
            database=settings.DB_NAME
        )

@login_required
def shelter_page(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        pets = request.POST.get('pets')
        phoneNumber = request.POST.get('phoneNumber')
        name = request.POST.get('name')

        cursor = mydb.cursor()
        cursor.execute("INSERT INTO shelters (address, pets, phoneNumber, name) VALUES (%s, %s, %s, %s)", (address, pets, phoneNumber, name))
        mydb.commit()

        return redirect('shelter_page')
    
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM shelters")
    shelters = cursor.fetchall()
    return render(request, 'shelter_page.html', {'shelters': shelters})

@login_required
def delete_shelter(request, shelter_id):
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM shelters WHERE shelter_id = %s", (shelter_id,))
    mydb.commit()

    return redirect('shelter_page')
