from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Vet
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
def vet_page(request):
    if request.method == 'POST':
        fName = request.POST.get('fName2')
        lName = request.POST.get('lName2')
        address = request.POST.get('address2')
        email = request.POST.get('email2')
        phoneNumber = request.POST.get('phoneNumber2')
        businessName = request.POST.get('businessName2')

        cursor = mydb.cursor()
        
        cursor.execute("INSERT INTO vets (phoneNumber, businessName, address, fName, lName, email) VALUES (%s, %s, %s, %s, %s, %s)", (phoneNumber, businessName, address, fName, lName, email))
        mydb.commit()

        return redirect('vet_page')

    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM vets")
    vets = cursor.fetchall()
    return render(request, 'vet_page.html', {'vets': vets})


@login_required
def delete_vet(request, vet_id):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM pets WHERE vet_id = %s", (vet_id,))
    pets = cursor.fetchall()  # Fetch all rows returned by the query
    if pets:  # Check if there are any related pets
        return redirect('error_page')

    cursor.execute("DELETE FROM vets WHERE vet_id = %s", (vet_id,))
    mydb.commit()

    return redirect('vet_page')

@login_required
def edit_vet(request, vet_id):
    if request.method == 'POST':
        address = request.POST.get('address')
        fName = request.POST.get('fName')
        phoneNumber = request.POST.get('phoneNumber')
        businessName = request.POST.get('businessName')
        lName = request.POST.get('lName')
        email = request.POST.get('email')

        cursor = mydb.cursor()
        cursor.execute("UPDATE vets SET address=%s, fName=%s, phoneNumber=%s, lName=%s, businessName=%s, email=%s WHERE vet_id=%s", (address, fName, phoneNumber, lName, businessName, email, vet_id))
        mydb.commit()

        return redirect('vet_page')
    
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM vets WHERE vet_id = %s", (vet_id,))
    vets = cursor.fetchone()

    return render(request, 'edit_vet.html', {'vet': vets})

@login_required
def sort_vet(request):
    address = request.GET.get('addressS')
    vet_id = request.GET.get('vet_idS')
    fName = request.GET.get('fNameS')
    lName = request.GET.get('lNameS')
    email = request.GET.get('emailS')
    phoneNumber = request.GET.get('phoneNumberS')
    businessName = request.GET.get('businessS')
    
    
    cursor = mydb.cursor(dictionary=True)
    query = "SELECT * FROM vets WHERE 1=1" 
    
    # Adding filters based on provided criteria
    if address:
        query += f" AND address LIKE '%{address}%'"
    if email:
        query += f" AND email LIKE '%{email}%'"
    if vet_id:
        query += f" AND vet_id LIKE '{vet_id}'"
    if phoneNumber:
        query += f" AND phoneNumber LIKE '%{phoneNumber}%'"
    if businessName:
        query += f" AND businessName LIKE '%{businessName}%'"
    if fName:
        query += f" AND fName LIKE '%{fName}%'"
    if lName:
        query += f" AND lName LIKE '%{lName}%'"
    
    cursor.execute(query)
    vets = cursor.fetchall()

    return render(request, 'vet_page.html', {'vets': vets})