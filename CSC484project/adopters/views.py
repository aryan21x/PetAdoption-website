from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Adopter
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
def adopter_page(request):
    if request.method == 'POST':
        firstName = request.POST.get('fName2')
        lastName = request.POST.get('lName2')
        email = request.POST.get('email2')
        address = request.POST.get('address2')
        pets = request.POST.get('pets2')
        phoneNumber = request.POST.get('phoneNumber2')

        cursor = mydb.cursor()
        cursor.execute("INSERT INTO adopters (fName, lName, email, address, pets, phoneNumber) VALUES (%s, %s, %s, %s, %s, %s)", (firstName, lastName, email, address, pets, phoneNumber))
        mydb.commit()

        return redirect('adopter_page')
    
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM adopters")
    adopters = cursor.fetchall()
    return render(request, 'adopter_page.html', {'adopters': adopters})

@login_required
def delete_adopter(request, adopt_id):
    cursor = mydb.cursor()
    
    cursor.execute("SELECT * FROM pets WHERE adoptered = 1 AND adopt_id = %s", (adopt_id,))
    pets = cursor.fetchall()  # Fetch all rows returned by the query
    if pets:  # Check if there are any related pets
        return redirect('error_page')
    
    cursor.execute("DELETE FROM adopters WHERE adopt_id = %s", (adopt_id,))
    mydb.commit()

    return redirect('adopter_page')


@login_required
def edit_adopter(request, adopt_id):
    if request.method == 'POST':
        firstName = request.POST.get('fName')
        lastName = request.POST.get('lName')
        email = request.POST.get('email')
        address = request.POST.get('address')
        pets = request.POST.get('pets')
        phoneNumber = request.POST.get('phoneNumber')

        cursor = mydb.cursor()
        cursor.execute("UPDATE adopters SET fName=%s, lName=%s, email=%s, address=%s, pets=%s, phoneNumber=%s WHERE adopt_id=%s", (firstName, lastName, email, address, pets, phoneNumber,adopt_id))
        mydb.commit()

        return redirect('adopter_page')
    
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM adopters WHERE adopt_id = %s", (adopt_id,))
    adopters = cursor.fetchone()

    return render(request, 'edit_adopter.html', {'adopter': adopters})


@login_required
def sort_adopter(request):
    firstName = request.GET.get('fName')
    lastName = request.GET.get('lName')
    email = request.GET.get('email')
    address = request.GET.get('address')
    pets = request.GET.get('pets')
    phoneNumber = request.GET.get('phoneNumber')
    
    cursor = mydb.cursor(dictionary=True)
    query = "SELECT * FROM adopters WHERE 1=1" 

    if address:
        query += f" AND address LIKE '%{address}%'"
    if pets:
        query += f" AND pets LIKE '{pets}'"
    if phoneNumber:
        query += f" AND phoneNumber LIKE '{phoneNumber}'"
    if firstName:
        query += f" AND fName LIKE '%{firstName}%'"
    if  lastName:
        query += f" AND lName LIKE '%{lastName}%'"
    if  email:
        query += f" AND email LIKE '%{email}%'"
    
    cursor.execute(query)
    adopters = cursor.fetchall()

    return render(request, 'adopter_page.html', {'adopters': adopters})



