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
    
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM workers")
    workers = cursor.fetchall()
    return render(request, 'worker_page.html', {'workers': workers})


@login_required
def delete_worker(request, worker_id):
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM workers WHERE worker_id = %s", (worker_id,))
    mydb.commit()

    return redirect('worker_page')

@login_required
def edit_worker(request, worker_id):
    if request.method == 'POST':
        address = request.POST.get('address')
        pets = request.POST.get('pets')
        phoneNumber = request.POST.get('phoneNumber')
        name = request.POST.get('name')

        cursor = mydb.cursor()
        cursor.execute("UPDATE workers SET address=%s, pets=%s, phoneNumber=%s, name=%s WHERE worker_id=%s", (address, pets, phoneNumber, name, worker_id))
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
    
    
    cursor = mydb.cursor(dictionary=True)
    query = "SELECT * FROM workers WHERE 1=1" 
    
    # Adding filters based on provided criteria
    if address:
        query += f" AND address LIKE '%{address}%'"
    if shelter_id:
        query += f" AND shelter_id LIKE '%{shelter_id}%'"
    if fName:
        query += f" AND fName LIKE '%{fName}%'"
    if lName:
        query += f" AND lName LIKE '%{lName}%'"
    
    cursor.execute(query)
    workers = cursor.fetchall()

    return render(request, 'worker_page.html', {'workers': workers})