create database if not exists project;

use project;

drop table if exists user_table;
drop table if exists pets;
drop table if exists workers;
drop table if exists shelters;
drop table if exists adopters;
drop table if exists associatedBusinesses;
drop table if exists vets;


create table if not exists user_table
			(user_id int primary key auto_increment not null, username varchar(255) not null, 
            password varchar(255) not null);
            
create table if not exists shelters
			(shelter_id int primary key auto_increment not null, address varchar(255) not null, 
            pets int, phoneNumber double, name varchar(255) not null);
            
create table if not exists workers
			(worker_id int primary key auto_increment not null, fName varchar(255) not null, 
            lName varchar(255) not null,  email varchar(255), address varchar(255) not null, 
            shelter_id int,
			foreign key(shelter_id) references shelters(shelter_id),INDEX(shelter_id));
            
create table if not exists adopters
			(adopt_id int primary key auto_increment not null, fName varchar(255) not null, 
            lName varchar(255) not null,  email varchar(255), address varchar(255) not null, 
            pets int, phoneNumber double);            
            
create table if not exists associatedBusinesses
			(business_id int primary key auto_increment not null, address varchar(255) not null, 
            service varchar(255), phoneNumber double,  email varchar(255),  name varchar(255) not null);       
            
create table if not exists vets
			(vet_id int primary key auto_increment not null, fName varchar(255) not null, 
            lName varchar(255) not null,  email varchar(255), address varchar(255) not null, 
            phoneNumber double,
			businessName varchar(255));
            
create table if not exists pets
			(pet_id int primary key auto_increment not null, name varchar(255) not null, 
            breed varchar(255) not null, shelter_id int, foreign key(shelter_id) references shelters(shelter_id), 
            species varchar(255) not null, age int, adoptered bool, 
            worker_id int, vet_id int, adopt_id int,
            foreign key(worker_id) references workers(worker_id), foreign key(vet_id) references vets(vet_id),
            foreign key(adopt_id) references adopters(adopt_id));
        
-- Drop the existing image_path column
ALTER TABLE pets
DROP COLUMN image_path;

-- Add the new image_path column with the desired default value
ALTER TABLE pets
ADD COLUMN image_path VARCHAR(255) DEFAULT '';

-- Update image_path with new values
UPDATE pets
SET image_path = CONCAT('/static/images/', pet_id, '.jpg')
WHERE pet_id IS NOT NULL;

select *
from associatedbusinesses;