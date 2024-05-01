from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Pet
import mysql.connector
from django.conf import settings
from django.shortcuts import redirect
import os
import uuid

mydb = mysql.connector.connect(
            host=settings.DB_HOST,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
            database=settings.DB_NAME
        )

UPLOAD_FOLDER = 'pet_page\\static\\images'
SAVE_FOLDER = '/static/images'

# Create your views here.
@login_required
def pet_page(request):
    if request.method == 'POST':
        name = request.POST.get('name2')
        breed = request.POST.get('breed2')
        species = request.POST.get('species2')
        age = request.POST.get('age2')
        worker_id = request.POST.get('worker_id2')
        location = request.POST.get('location2')
        adopted = request.POST.get('adopted2')
        vet_id = request.POST.get('vet_id2')
        file = request.FILES.get('image')
        filepath = "/static/images/default.jpg"

        if file:
            filename = str(uuid.uuid4()) + '.jpg'
            filepath2 = os.path.join(settings.BASE_DIR, UPLOAD_FOLDER, filename)
            filepath = os.path.join(SAVE_FOLDER, filename)
            with open(filepath2, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM workers WHERE worker_id = %s", (worker_id,))
        workers = cursor.fetchall()  # Fetch all rows returned by the query
        if workers: 
            cursor.execute("SELECT * FROM vets WHERE vet_id = %s", (vet_id,))
            vets = cursor.fetchall()  # Fetch all rows returned by the query
            if vets:
                if adopted:
                    cursor.execute("SELECT * FROM adopters WHERE adopt_id = %s", (location,))
                    adopt = cursor.fetchall()  # Fetch all rows returned by the query
                    if adopt:
                        cursor.execute("INSERT INTO pets (name, breed, species, age, worker_id, adopt_id, adoptered, vet_id, image_path) VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s)", (name, breed, species, age, worker_id, location, 1,vet_id,filepath))
                        mydb.commit()
                        return redirect('pet_page')
                else:
                    cursor.execute("SELECT * FROM shelters WHERE shelter_id = %s", (location,))
                    shelter = cursor.fetchall()  # Fetch all rows returned by the query
                    if shelter:
                        cursor = mydb.cursor()
                        cursor.execute("INSERT INTO pets (name, breed, species, age, worker_id, shelter_id, adoptered, vet_id,image_path) VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s)", (name, breed, species, age, worker_id, location, 0,vet_id,filepath))
                        mydb.commit()
                        return redirect('pet_page')

        return redirect('not_found')
    
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pets")
    pets = cursor.fetchall()
    return render(request, 'pet_page.html', {'pets': pets})

@login_required
def sort_pet(request):
    name = request.GET.get('name')
    breed = request.GET.get('breed')
    species = request.GET.get('species')
    age = request.GET.get('age')
    adopted_needs_home = request.GET.get('adopted_needs_home')
    adopted_adopted = request.GET.get('adopted_adopted')
    workerId = request.GET.get('worker_id')
    vetId = request.GET.get('vet_id')
    location = request.GET.get('location')
    
    cursor = mydb.cursor(dictionary=True)
    query = "SELECT * FROM pets WHERE 1=1"
    
    # Adding filters based on provided criteria
    if name:
        query += f" AND name LIKE '%{name}%'"
    if breed:
        query += f" AND breed LIKE '%{breed}%'"
    if adopted_needs_home:
        if location:
            query += f" AND shelter_id LIKE '%{location}%'"
    if adopted_adopted:
        if location:
            query += f" AND adopt_id LIKE '%{location}%'"
    if workerId:
        query += f" AND worker_id LIKE '%{workerId}%'"
    if vetId:
        query += f" AND vet_id LIKE '{vetId}'"
    if species:
        query += f" AND species LIKE '%{species}%'"
    if age:
        query += f" AND age = {age}"
    if adopted_needs_home:
        query += f" AND adoptered = 0"
    if adopted_adopted:
        query += f" AND adoptered = 1"
    
    cursor.execute(query)
    pets = cursor.fetchall()

    return render(request, 'pet_page.html', {'pets': pets})

@login_required
def delete_pet(request, pet_id):
    # cursor = mydb.cursor(dictionary=True)
    # cursor.execute("SELECT * FROM pets WHERE pet_id = %s", (pet_id,))
    # pet = cursor.fetchone()

    # image_path = pet['image_path']
    # _, filename = os.path.split(image_path)
    # filepath = os.path.join(settings.BASE_DIR, filename)
    # if os.path.exists(filepath):
    #     os.remove(image_path)
    
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM pets WHERE pet_id = %s", (pet_id,))
    mydb.commit()

    return redirect('pet_page')


@login_required
def edit_pet(request, pet_id):
    if request.method == 'POST':
        name = request.POST.get('name')
        breed = request.POST.get('breed')
        worker_id = request.POST.get('worker_id')
        location = request.POST.get('location')
        adopted = request.POST.get('adopted')
        species = request.POST.get('species')
        age = request.POST.get('age')
        vet_id = request.POST.get('vet_id')

        if adopted:
            cursor = mydb.cursor()
            cursor.execute("UPDATE pets SET name=%s, breed=%s, worker_id=%s, adopt_id=%s, adoptered=%s, species=%s, age=%s, vet_id=%s WHERE pet_id=%s", (name, breed, worker_id, location, 1, species, age, vet_id, pet_id))
            mydb.commit()
        else:
            cursor = mydb.cursor()
            cursor.execute("UPDATE pets SET name=%s, breed=%s, worker_id=%s, shelter_id=%s, adoptered=%s, species=%s, age=%s, vet_id=%s WHERE pet_id=%s", (name, breed, worker_id, location, 0, species, age, vet_id, pet_id))
            mydb.commit()

        return redirect('pet_page')
    
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pets WHERE pet_id = %s", (pet_id,))
    pet = cursor.fetchone()

    return render(request, 'edit_pet.html', {'pet': pet})

