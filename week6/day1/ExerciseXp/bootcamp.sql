CREATE DATABASE bootcamp
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

 CREATE TABLE students(
 	students_id SERIAL PRIMARY KEY,
 	first_name VARCHAR (50) NOT NULL,
 	last_name VARCHAR (100) NOT NULL,
    birth_date date);

INSERT INTO students (first_name,last_name,birth_date)
VALUES('Marc','Benichou','02/11/1998'),
	  ('Yoan','Cohen','03/12/2010'),
	  ('Lea','Benichou','27/07/1987'),
	  ('Amelia','Dux','07/04/1996'),
	  ('David','Grez','14/06/2003'),
	  ('Omer','Simpson','03/10/1980');

-- Fetch all of the data from the table.
SELECT * FROM students;

-- Fetch all of the students first_names and last_names.
SELECT "first_name", "last_name" FROM students;

-- For the following questions, only fetch the first_names and last_names of the students.
-- Fetch the student which id is equal to 2
SELECT "first_name", "last_name" FROM students where students_id = 2; 

-- Fetch the student whose last_name is Benichou AND first_name is Marc.
SELECT "first_name", "last_name" FROM students where last_name = 'Benichou' and first_name = 'Marc'  ;

--Fetch the students whose last_names are Benichou OR first_names are Marc.
SELECT "first_name", "last_name" FROM students where last_name = 'Benichou' OR first_name = 'Marc'  ;

-- Fetch the students whose first_names contain the letter a
SELECT "first_name", "last_name" FROM students where first_name LIKE '%a%' ;

-- Fetch the students whose first_names start with the letter a.
SELECT "first_name", "last_name" FROM students where lower(first_name) LIKE 'a%' ;

-- Fetch the students whose first_names end with the letter a.
SELECT "first_name", "last_name" FROM students where first_name LIKE '%a' ;

-- Fetch the students whose second to last letter of their first_names are a (Example: Leah)
SELECT "first_name", "last_name" FROM students where first_name LIKE '%a%' ;

-- Fetch the students whose id’s are equal to 1 AND 3
SELECT "first_name", "last_name" FROM students where students_id = 1 OR students_id = 3 ;

-- Fetch the students whose birth_dates are equal to or come after 1/01/2000
SELECT "first_name", "last_name" FROM students where birth_date >= '1/01/2000' ; 
