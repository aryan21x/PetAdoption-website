use project;


-- get some users
INSERT INTO user_table (username, password)
VALUES 
('Joe', 'Rogan'),
('Gandhi', 'SoHungry'),
('Elizabeth', 'EmpressOfIndia');

-- Mock data for shelters
INSERT INTO shelters (address, pets, phoneNumber, name) VALUES 
('123 Main St', 20, 1234567890, 'Main Street Animal Shelter'),
('456 Oak Ave', 15, 9876543210, 'Oak Avenue Pet Rescue'),
('789 Maple Rd', 30, 1112223333, 'Maple Road Animal Haven');

-- Mock data for workers
INSERT INTO workers (fName, lName, email, address, shelter_id) VALUES 
('John', 'Doe', 'john.doe@example.com', '123 Main St', 1),
('Jane', 'Smith', 'jane.smith@example.com', '456 Oak Ave', 2),
('Michael', 'Johnson', 'michael.johnson@example.com', '789 Maple Rd', 3);

-- Mock data for adopters
INSERT INTO adopters (fName, lName, email, address, pets, phoneNumber) VALUES 
('Alice', 'Brown', 'alice.brown@example.com', '101 Elm St', 1, 5551234567),
('Bob', 'Davis', 'bob.davis@example.com', '202 Pine Ave', 2, 5552345678),
('Carol', 'Evans', 'carol.evans@example.com', '303 Cedar Rd', 0, 5553456789);

-- Mock data for associatedBusinesses
INSERT INTO associatedBusinesses (address, service, phoneNumber, email, name) VALUES 
('789 Oak St', 'Veterinary Services', 987654321, 'vetclinic@example.com', 'Oak Street Veterinary Clinic'),
('456 Maple Ave', 'Pet Grooming', 123456789, 'petgrooming@example.com', 'Maple Avenue Pet Spa'),
('123 Pine Rd', 'Pet Supplies', 456789123, 'petsupplies@example.com', 'Pine Road Pet Emporium');

-- Mock data for vets
INSERT INTO vets (fName, lName, email, address, businessName) VALUES 
('Emily', 'White', 'emily.white@example.com', '789 Oak St', 'Oak Street Veterinary Clinic'),
('David', 'Brown', 'david.brown@example.com', '456 Maple Ave', 'Maple Avenue Pet Spa'),
('Sarah', 'Jones', 'sarah.jones@example.com', '123 Pine Rd', 'Pine Road Pet Emporium');

-- Mock data for pets
INSERT INTO pets (name, breed, shelter_id, species, age, adoptered, worker_id, vet_id, adopt_id) VALUES 
('Buddy', 'Labrador Retriever', 1, 'Dog', 3, 0, 1, 1, NULL),
('Fluffy', 'Persian', 2, 'Cat', 2, 0, 2, NULL, NULL),
('Max', 'German Shepherd', 3, 'Dog', 4, 0, 3, 3, 1),
('Smokey', 'Siamese', 2, 'Cat', 5, 1, 2, NULL, NULL);