use project;

-- get some users
INSERT INTO user_table (username, password)
VALUES 
('Joe', 'Rogan'),
('Gandhi', 'SoHungry'),
('Elizabeth', 'EmpressOfIndia'),
('1','2');

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


-- Additional 20 seeding of data
-- Insert 20 rows of data into the user_table
INSERT INTO user_table (username, password)
VALUES 
('Joe', 'Rogan'),
('Gandhi', 'SoHungry'),
('Elizabeth', 'EmpressOfIndia'),
('1','2'),
('Marie', 'Curie'),
('Leonardo', 'DaVinci'),
('Cleopatra', 'QueenOfNile'),
('Albert', 'Einstein'),
('Isaac', 'Newton'),
('Galileo', 'Galilei'),
('Nikola', 'Tesla'),
('Ada', 'Lovelace'),
('Charles', 'Darwin'),
('Stephen', 'Hawking'),
('Marie', 'Antoinette'),
('Wolfgang', 'Mozart'),
('Jane', 'Austen'),
('William', 'Shakespeare'),
('Vincent', 'VanGogh'),
('Pablo', 'Picasso'),
('Amelia', 'Earhart'),
('Neil', 'Armstrong'),
('Rosa', 'Parks'),
('Mahatma', 'Gandhi');

-- Insert 20 rows of data into the shelters
INSERT INTO shelters (address, pets, phoneNumber, name) VALUES 
('123 Main St', 20, 1234567890, 'Main Street Animal Shelter'),
('456 Oak Ave', 15, 9876543210, 'Oak Avenue Pet Rescue'),
('789 Maple Rd', 30, 1112223333, 'Maple Road Animal Haven'),
('111 Elm St', 10, 1111111111, 'Elm Street Animal Rescue'),
('222 Pine Ave', 25, 2222222222, 'Pine Avenue Pet Shelter'),
('333 Cedar Rd', 20, 3333333333, 'Cedar Road Animal Sanctuary'),
('444 Birch Blvd', 15, 4444444444, 'Birch Boulevard Pet Haven'),
('555 Willow Ln', 30, 5555555555, 'Willow Lane Animal Refuge'),
('666 Spruce Dr', 18, 6666666666, 'Spruce Drive Pet Adoption Center'),
('777 Walnut Ct', 22, 7777777777, 'Walnut Court Animal Welfare'),
('888 Chestnut Ave', 28, 8888888888, 'Chestnut Avenue Pet Rescue'),
('999 Ash St', 12, 9999999999, 'Ash Street Animal Shelter'),
('1010 Oak Rd', 17, 1010101010, 'Oak Road Pet Adoption');

-- Insert 20 rows of data into the workers
INSERT INTO workers (fName, lName, email, address, shelter_id) VALUES 
('John', 'Doe', 'john.doe@example.com', '123 Main St', 1),
('Jane', 'Smith', 'jane.smith@example.com', '456 Oak Ave', 8),
('Michael', 'Johnson', 'michael.johnson@example.com', '789 Maple Rd', 3),
('Emily', 'Johnson', 'emily.johnson@example.com', '111 Elm St', 1),
('Daniel', 'Martinez', 'daniel.martinez@example.com', '222 Pine Ave', 9),
('Olivia', 'Anderson', 'olivia.anderson@example.com', '333 Cedar Rd', 3),
('Liam', 'Taylor', 'liam.taylor@example.com', '444 Birch Blvd', 1),
('Sophia', 'Thomas', 'sophia.thomas@example.com', '555 Willow Ln', 8),
('Benjamin', 'Hernandez', 'benjamin.hernandez@example.com', '666 Spruce Dr', 3),
('Ava', 'Walker', 'ava.walker@example.com', '777 Walnut Ct', 1),
('Lucas', 'Wright', 'lucas.wright@example.com', '888 Chestnut Ave', 8),
('Mia', 'Roberts', 'mia.roberts@example.com', '999 Ash St', 3),
('Jackson', 'Clark', 'jackson.clark@example.com', '1010 Oak Rd', 7),
('Alexander', 'Lewis', 'alexander.lewis@example.com', '111 Elm St', 2),
('Charlotte', 'Lee', 'charlotte.lee@example.com', '222 Pine Ave', 3),
('James', 'Hall', 'james.hall@example.com', '333 Cedar Rd', 1),
('Amelia', 'Young', 'amelia.young@example.com', '444 Birch Blvd', 2),
('Evelyn', 'Harris', 'evelyn.harris@example.com', '555 Willow Ln', 5),
('Michael', 'Scott', 'michael.scott@example.com', '666 Spruce Dr', 1),
('Emma', 'Green', 'emma.green@example.com', '777 Walnut Ct', 6);

SELECT *
FROM workers;
-- Insert 20 rows of data into the adopters
INSERT INTO adopters (fName, lName, email, address, pets, phoneNumber) VALUES 
('Alice', 'Brown', 'alice.brown@example.com', '101 Elm St', 1, 5551234567),
('Bob', 'Davis', 'bob.davis@example.com', '202 Pine Ave', 2, 5552345678),
('Carol', 'Evans', 'carol.evans@example.com', '303 Cedar Rd', 0, 5553456789),
('Liam', 'Johnson', 'liam.johnson@example.com', '1212 Elm St', 0, 5551111111),
('Emma', 'Martinez', 'emma.martinez@example.com', '2323 Pine Ave', 1, 5552222222),
('Ava', 'Anderson', 'ava.anderson@example.com', '3434 Cedar Rd', 2, 5553333333),
('Noah', 'Taylor', 'noah.taylor@example.com', '4545 Birch Blvd', 0, 5554444444),
('Isabella', 'Thomas', 'isabella.thomas@example.com', '5656 Willow Ln', 1, 5555555555),
('Sophia', 'Hernandez', 'sophia.hernandez@example.com', '6767 Spruce Dr', 0, 5556666666),
('Mason', 'Walker', 'mason.walker@example.com', '7878 Walnut Ct', 3, 5557777777),
('Harper', 'Wright', 'harper.wright@example.com', '8989 Chestnut Ave', 1, 5558888888),
('Evelyn', 'Roberts', 'evelyn.roberts@example.com', '9090 Ash St', 0, 5559999999),
('Liam', 'Clark', 'liam.clark@example.com', '1010 Oak Rd', 2, 5551010101),
('Emma', 'Lewis', 'emma.lewis@example.com', '1111 Elm St', 1, 5551212121),
('Oliver', 'Lee', 'oliver.lee@example.com', '1212 Pine Ave', 0, 5551313131),
('Amelia', 'Hall', 'amelia.hall@example.com', '1313 Cedar Rd', 2, 5551414141),
('Mia', 'Young', 'mia.young@example.com', '1414 Birch Blvd', 1, 5551515151),
('Lucas', 'Harris', 'lucas.harris@example.com', '1515 Willow Ln', 0, 5551616161),
('Sophia', 'Scott', 'sophia.scott@example.com', '1616 Spruce Dr', 1, 5551717171),
('Isabella', 'Green', 'isabella.green@example.com', '1717 Walnut Ct', 0, 5551818181);

-- Insert 20 rows of data into the associatedBusinesses
INSERT INTO associatedBusinesses (address, service, phoneNumber, email, name) VALUES 
('789 Oak St', 'Veterinary Services', 987654321, 'vetclinic@example.com', 'Oak Street Veterinary Clinic'),
('456 Maple Ave', 'Pet Grooming', 123456789, 'petgrooming@example.com', 'Maple Avenue Pet Spa'),
('123 Pine Rd', 'Pet Supplies', 456789123, 'petsupplies@example.com', 'Pine Road Pet Emporium'),
('321 Oak St', 'Veterinary Services', 987654321, 'vetclinic@example.com', 'Oak Street Veterinary Clinic II'),
('654 Maple Ave', 'Pet Grooming', 123456789, 'petgrooming@example.com', 'Maple Avenue Pet Spa II'),
('321 Pine Rd', 'Pet Supplies', 456789123, 'petsupplies@example.com', 'Pine Road Pet Emporium II'),
('147 Pine St', 'Veterinary Services', 987654321, 'vetclinic@example.com', 'Pine Street Veterinary Clinic'),
('258 Maple Ave', 'Pet Grooming', 123456789, 'petgrooming@example.com', 'Maple Avenue Pet Spa III'),
('369 Pine Rd', 'Pet Supplies', 456789123, 'petsupplies@example.com', 'Pine Road Pet Emporium III'),
('753 Oak St', 'Veterinary Services', 987654321, 'vetclinic@example.com', 'Oak Street Veterinary Clinic III'),
('852 Maple Ave', 'Pet Grooming', 123456789, 'petgrooming@example.com', 'Maple Avenue Pet Spa IV'),
('951 Pine Rd', 'Pet Supplies', 456789123, 'petsupplies@example.com', 'Pine Road Pet Emporium IV'),
('159 Oak St', 'Veterinary Services', 987654321, 'vetclinic@example.com', 'Oak Street Veterinary Clinic IV'),
('101 Pine St', 'Veterinary Services', 987654321, 'vetclinic@example.com', 'Pine Street Veterinary Clinic II'),
('456 Oak St', 'Pet Grooming', 123456789, 'petgrooming@example.com', 'Oak Street Pet Spa'),
('321 Elm Rd', 'Pet Supplies', 456789123, 'petsupplies@example.com', 'Elm Road Pet Emporium'),
('789 Elm St', 'Veterinary Services', 987654321, 'vetclinic@example.com', 'Elm Street Veterinary Clinic'),
('741 Pine Ave', 'Pet Grooming', 123456789, 'petgrooming@example.com', 'Pine Avenue Pet Spa V'),
('123 Cedar Rd', 'Pet Supplies', 456789123, 'petsupplies@example.com', 'Cedar Road Pet Emporium'),
('852 Oak St', 'Veterinary Services', 987654321, 'vetclinic@example.com', 'Oak Street Veterinary Clinic V');

-- Insert 20 rows of data into the vets
INSERT INTO vets (fName, lName, email, address, phoneNumber, businessName) VALUES 
('Emily', 'White', 'emily.white@example.com', '789 Oak St', 987654321, 'Oak Street Veterinary Clinic'),
('David', 'Brown', 'david.brown@example.com', '456 Maple Ave', 123456789, 'Maple Avenue Pet Spa'),
('Sarah', 'Jones', 'sarah.jones@example.com', '123 Pine Rd', 456789123, 'Pine Road Pet Emporium'),
('Sophie', 'Brown', 'sophie.brown@example.com', '321 Oak St', 987654321, 'Oak Street Veterinary Clinic II'),
('Liam', 'Davis', 'liam.davis@example.com', '654 Maple Ave', 123456789, 'Maple Avenue Pet Spa II'),
('Emma', 'Evans', 'emma.evans@example.com', '321 Pine Rd', 456789123, 'Pine Road Pet Emporium II'),
('Oliver', 'Garcia', 'oliver.garcia@example.com', '147 Pine St', 987654321, 'Pine Street Veterinary Clinic'),
('Ava', 'Harris', 'ava.harris@example.com', '258 Maple Ave', 123456789, 'Maple Avenue Pet Spa III'),
('Noah', 'Jackson', 'noah.jackson@example.com', '369 Pine Rd', 456789123, 'Pine Road Pet Emporium III'),
('Isabella', 'King', 'isabella.king@example.com', '753 Oak St', 987654321, 'Oak Street Veterinary Clinic III'),
('Mia', 'Lee', 'mia.lee@example.com', '852 Maple Ave', 123456789, 'Maple Avenue Pet Spa IV'),
('James', 'Lopez', 'james.lopez@example.com', '951 Pine Rd', 456789123, 'Pine Road Pet Emporium IV'),
('Lucas', 'Martin', 'lucas.martin@example.com', '159 Oak St', 987654321, 'Oak Street Veterinary Clinic IV'),
('Sophia', 'Martinez', 'sophia.martinez@example.com', '101 Pine St', 123456789, 'Pine Street Veterinary Clinic II'),
('Ethan', 'Thompson', 'ethan.thompson@example.com', '456 Oak St', 456789123, 'Oak Street Pet Spa'),
('Isabella', 'Adams', 'isabella.adams@example.com', '321 Elm Rd', 987654321, 'Elm Road Pet Emporium'),
('James', 'Johnson', 'james.johnson@example.com', '789 Elm St', 123456789, 'Elm Street Veterinary Clinic'),
('Liam', 'Brown', 'liam.brown@example.com', '741 Pine Ave', 456789123, 'Pine Avenue Pet Spa V'),
('Ava', 'Martinez', 'ava.martinez@example.com', '123 Cedar Rd', 987654321, 'Cedar Road Pet Emporium'),
('Mason', 'Garcia', 'mason.garcia@example.com', '852 Oak St', 123456789, 'Oak Street Veterinary Clinic V');

-- Insert 20 rows of data into the pets
INSERT INTO pets (name, breed, shelter_id, species, age, adoptered, worker_id, vet_id, adopt_id) VALUES 
('Rocky', 'Poodle', 1, 'Dog', 2, 0, 10, 1, NULL),
('Bella', 'Bulldog', 1, 'Dog', 5, 0, 4, 2, 2),
('Charlie', 'Beagle', 1, 'Dog', 3, 1, 5, NULL, NULL),
('Luna', 'Siamese', 2, 'Cat', 1, 0, 16, 4, NULL),
('Daisy', 'Golden Retriever', 2, 'Dog', 4, 0, 17, 5, 3),
('Loki', 'Maine Coon', 2, 'Cat', 2, 1, 8, NULL, NULL),
('Molly', 'Labrador Retriever', 3, 'Dog', 6, 0, 9, 7, 4),
('Sadie', 'Ragdoll', 3, 'Cat', 3, 0, 2, 8, NULL),
('Bailey', 'Siberian Husky', 3, 'Dog', 4, 1, 1, NULL, NULL),
('Toby', 'American Shorthair', 1, 'Cat', 5, 0, 3, 10, 5),
('Jack', 'Boxer', 1, 'Dog', 3, 0, 3, 9, 6),
('Milo', 'Dachshund', 1, 'Dog', 14, 1, 3, NULL, NULL),
('Max', 'Sphynx', 2, 'Cat', 4, 0, 4, 11, 7),
('Cooper', 'Yorkshire Terrier', 2, 'Dog', 1, 0, 5, 12, NULL),
('Buddy', 'Bengal', 2, 'Cat', 3, 1, 6, NULL, NULL),
('Harley', 'Pomeranian', 3, 'Dog', 5, 0, 7, 13, 8),
('Lucy', 'Scottish Fold', 3, 'Cat', 2, 0, 8, 14, NULL),
('Stella', 'Doberman Pinscher', 3, 'Dog', 4, 1, 9, NULL, NULL),
('Bear', 'British Shorthair', 1, 'Cat', 3, 0, 2, 15, 9),
('Teddy', 'Rottweiler', 1, 'Dog', 2, 0, 1, 16, NULL),
('Zoe', 'Great Dane', 1, 'Dog', 1, 1, 2, NULL, NULL);

use project;
SELECT *
from pets;