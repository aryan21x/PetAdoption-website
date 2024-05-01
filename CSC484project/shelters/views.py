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
        address = request.POST.get('address2')
        pets = request.POST.get('pets2')
        phoneNumber = request.POST.get('phoneNumber2')
        name = request.POST.get('name2')

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

    cursor.execute("SELECT * FROM workers WHERE shelter_id = %s", (shelter_id,))
    workers = cursor.fetchall()  # Fetch all rows returned by the query
    if workers:  # Check if there are any related pets
        return redirect('error_page')
    
    cursor.execute("SELECT * FROM pets WHERE adoptered = 0 AND shelter_id = %s", (shelter_id,))
    pets = cursor.fetchall()  # Fetch all rows returned by the query
    if pets:  # Check if there are any related pets
        return redirect('error_page')

    cursor.execute("DELETE FROM shelters WHERE shelter_id = %s", (shelter_id,))
    mydb.commit()

    return redirect('shelter_page')


@login_required
def edit_shelter(request, shelter_id):
    if request.method == 'POST':
        address = request.POST.get('address')
        pets = request.POST.get('pets')
        phoneNumber = request.POST.get('phoneNumber')
        name = request.POST.get('name')

        cursor = mydb.cursor()
        cursor.execute("UPDATE shelters SET address=%s, pets=%s, phoneNumber=%s, name=%s WHERE shelter_id=%s", (address, pets, phoneNumber, name, shelter_id))
        mydb.commit()

        return redirect('shelter_page')
    
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM shelters WHERE shelter_id = %s", (shelter_id,))
    shelters = cursor.fetchone()

    return render(request, 'edit_shelter.html', {'shelter': shelters})


@login_required
def sort_shelter(request):
    address = request.GET.get('address')
    pets = request.GET.get('pets')
    phoneNumber = request.GET.get('phoneNumber')
    name = request.GET.get('name')
    
    cursor = mydb.cursor(dictionary=True)
    query = "SELECT * FROM shelters WHERE 1=1" 
    
    # Adding filters based on provided criteria
    if address:
        query += f" AND address LIKE '%{address}%'"
    if pets:
        query += f" AND pets LIKE '{pets}'"
    if phoneNumber:
        query += f" AND phoneNumber LIKE '{phoneNumber}'"
    if name:
        query += f" AND name LIKE '%{name}%'"
    
    cursor.execute(query)
    shelters = cursor.fetchall()

    return render(request, 'shelter_page.html', {'shelters': shelters})


