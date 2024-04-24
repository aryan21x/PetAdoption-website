from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Pet
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
def pet_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        breed = request.POST.get('breed')
        species = request.POST.get('species')
        age = request.POST.get('age')

        cursor = mydb.cursor()
        cursor.execute("INSERT INTO pets (name, breed, species, age) VALUES (%s, %s, %s,%s)", (name, breed, species, age))
        mydb.commit()

        return redirect('pet_page')
    
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pets")
    pets = cursor.fetchall()
    return render(request, 'pet_page.html', {'pets': pets})

@login_required
def delete_pet(request, pet_id):
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM pets WHERE pet_id = %s", (pet_id,))
    mydb.commit()

    return redirect('pet_page')


# Not implemented Yet
@login_required
def edit_pet(request, pet_id):
    if request.method == 'POST':
        name = request.POST.get('name')
        breed = request.POST.get('breed')
        species = request.POST.get('species')
        age = request.POST.get('age')

        cursor = mydb.cursor()
        cursor.execute("UPDATE pets SET name=%s, breed=%s, species=%s, age=%s WHERE pet_id=%s", (name, breed, species, age, pet_id))
        mydb.commit()

        return redirect('pet_page')

