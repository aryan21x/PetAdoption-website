from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import AssociatedBusiness
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
def business_page(request):
    if request.method == 'POST':
        address = request.POST.get('address2')
        service = request.POST.get('service2')
        phoneNumber = request.POST.get('phoneNumber2')
        email = request.POST.get('email2')
        name = request.POST.get('name2')


        cursor = mydb.cursor()
        cursor.execute("INSERT INTO associatedBusinesses (address, service, phoneNumber, email, name) VALUES (%s, %s, %s, %s, %s)", (address, service, phoneNumber, email, name))
        mydb.commit()

        return redirect('business_page')
    
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM associatedBusinesses")
    businesses = cursor.fetchall()
    return render(request, 'business_page.html', {'businesses': businesses})

@login_required
def delete_business(request, business_id):
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM associatedBusinesses WHERE business_id = %s", (business_id,))
    mydb.commit()

    return redirect('business_page')


@login_required
def edit_business(request, business_id):
    if request.method == 'POST':
        address = request.POST.get('address')
        service = request.POST.get('service')
        phoneNumber = request.POST.get('phoneNumber')
        email = request.POST.get('email')
        name = request.POST.get('name')

        cursor = mydb.cursor()
        cursor.execute("UPDATE associatedBusinesses SET address=%s, service=%s, phoneNumber=%s, email=%s, name=%s WHERE business_id=%s", (address,service, phoneNumber,email, name, business_id))
        mydb.commit()

        return redirect('business_page')
    
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM associatedBusinesses WHERE business_id = %s", (business_id,))
    businesses = cursor.fetchone()

    return render(request, 'edit_business.html', {'business': businesses})


@login_required
def sort_business(request):
    address = request.GET.get('address')
    service = request.GET.get('service')
    phoneNumber = request.GET.get('phoneNumber')
    email = request.GET.get('email')
    name = request.GET.get('name')
    
    cursor = mydb.cursor(dictionary=True)
    query = "SELECT * FROM associatedBusinesses WHERE 1=1" 
    
    # Adding filters based on provided criteria
    if address:
        query += f" AND address LIKE '%{address}%'"
    if service:
        query += f" AND service LIKE '%{service}%'"
    if phoneNumber:
        query += f" AND phoneNumber LIKE '{phoneNumber}'"
    if email:
        query += f" AND email LIKE '%{email}%'"
    if name:
        query += f" AND name LIKE '%{name}%'"
    
    cursor.execute(query)
    businesses = cursor.fetchall()

    return render(request, 'business_page.html', {'businesses': businesses})



