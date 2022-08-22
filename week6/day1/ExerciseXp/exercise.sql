-- Database: public

-- DROP DATABASE IF EXISTS public;

CREATE DATABASE public
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

CREATE TABLE items(
 item_id SERIAL PRIMARY KEY,
 Description VARCHAR (100) NOT NULL,
 price INTEGER NOT NULL);

INSERT INTO items (description, price)
VALUES('Small Desk',100),
		('Large Desk',300),
		('Fan',80);

 CREATE TABLE customers(
 	customer_id SERIAL PRIMARY KEY,
 	first_name VARCHAR (50) NOT NULL,
 	last_name VARCHAR (100) NOT NULL);

INSERT INTO customers (first_name,last_name)
VALUES('Greg','Jones'),
	  ('Sandra','Jones'),
	  ('Scott','Scott'),
	  ('Trevor','Green'),
	  ('Melanie','Johnson');

-- Use SQL to fetch the following data from the database:
-- All the items.
Select * from items

-- All the items with a price above 80 (80 not included).
SELECT * FROM items where price > 80;

-- All the items with a price below 300. (300 included)
SELECT * FROM items where price <= 300;

-- All customers whose last name is ‘Smith’ (What will be your outcome?).
SELECT * FROM customers where last_name  = 'Smith';

-- All customers whose last name is ‘Jones’.
SELECT * FROM customers where last_name  = 'Jones';

-- All customers whose firstname is not 'Scott’.
SELECT * FROM customers where last_name  != 'Scott';



