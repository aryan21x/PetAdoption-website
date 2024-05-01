from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Worker
import mysql.connector
from django.conf import settings
from django.shortcuts import redirect

mydb = mysql.connector.connect(
            host=settings.DB_HOST,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
            database=settings.DB_NAME
        )

# Create your views here.
@login_required
def worker_page(request):
    if request.method == 'POST':
        address = request.POST.get('address2')
        fName = request.POST.get('fName2')
        shelter_id = request.POST.get('shelter_id2')
        lName = request.POST.get('lName2')
        email = request.POST.get('email2')


        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM shelters WHERE shelter_id = %s", (shelter_id,))
        shelters = cursor.fetchall()  # Fetch all rows returned by the query
        if shelters: 
            cursor.execute("INSERT INTO workers (shelter_id, address, fName, lName, email) VALUES (%s, %s, %s, %s, %s)", (shelter_id, address, fName, lName, email))
            mydb.commit()

            return redirect('worker_page')


        return redirect('not_found')

    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM workers")
    workers = cursor.fetchall()
    return render(request, 'worker_page.html', {'workers': workers})


@login_required
def delete_worker(request, worker_id):
    cursor = mydb.cursor()

    cursor.execute("SELECT * FROM pets WHERE worker_id = %s", (worker_id,))
    pets = cursor.fetchall()  # Fetch all rows returned by the query
    if pets:  # Check if there are any related pets
        return redirect('error_page')

    cursor.execute("DELETE FROM workers WHERE worker_id = %s", (worker_id,))
    mydb.commit()

    return redirect('worker_page')

@login_required
def edit_worker(request, worker_id):
    if request.method == 'POST':
        address = request.POST.get('address2')
        fName = request.POST.get('fName2')
        shelter_id = request.POST.get('shelter_id2')
        lName = request.POST.get('lName2')
        email = request.POST.get('email2')

        cursor = mydb.cursor()
        cursor.execute("UPDATE workers SET address=%s, fName=%s, shelter_id=%s, lName=%s WHERE worker_id=%s", (address, fName, shelter_id, lName, worker_id))
        mydb.commit()

        return redirect('worker_page')
    
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM workers WHERE worker_id = %s", (worker_id,))
    workers = cursor.fetchone()

    return render(request, 'edit_worker.html', {'worker': workers})

@login_required
def sort_worker(request):
    address = request.GET.get('address')
    shelter_id = request.GET.get('shelter_id')
    fName = request.GET.get('fName')
    lName = request.GET.get('lName')
    email = request.GET.get('email')
    worker_id = request.GET.get('worker_id')
    
    
    cursor = mydb.cursor(dictionary=True)
    query = "SELECT * FROM workers WHERE 1=1" 
    
    # Adding filters based on provided criteria
    if address:
        query += f" AND address LIKE '%{address}%'"
    if email:
        query += f" AND email LIKE '%{email}%'"
    if worker_id:
        query += f" AND worker_id LIKE '%{worker_id}%'"
    if shelter_id:
        query += f" AND shelter_id LIKE '%{shelter_id}%'"
    if fName:
        query += f" AND fName LIKE '%{fName}%'"
    if lName:
        query += f" AND lName LIKE '%{lName}%'"
    
    cursor.execute(query)
    workers = cursor.fetchall()

    return render(request, 'worker_page.html', {'workers': workers})