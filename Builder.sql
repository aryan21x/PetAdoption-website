create database if not exists project;

use project;

create table if not exists user_table
			(user_id int primary key auto_increment not null, username varchar(255) not null, 
            password varchar(255) not null);
            
create table if not exists pets
			(pet_id int primary key auto_increment not null, name varchar(255) not null, 
            breed varchar(255) not null, );
            
-- get some users
INSERT INTO user_table (username, password)
VALUES 
('Joe', 'Rogan'),
('Gandhi', 'SoHungry'),
('Elizabeth', 'EmpressOfIndia'),
('1','2');
