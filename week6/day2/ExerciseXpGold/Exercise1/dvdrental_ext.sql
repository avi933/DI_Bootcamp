-- Find out how many films there are for each rating
SELECT  rating,
   count(rating)
FROM 
   film
GROUP BY 
   rating;

-- Get a list of all the movies that have a rating of G or PG-13
SELECT title, rating 
FROM film
WHERE rating = 'G' or rating = 'PG-13'
-- Filter this list further: look for only movies that are under 2 hours long
-- and whose rental price (rental_rate) is under 3.00. Sort the list alphabetically.
SELECT title, rating, length, rental_rate
FROM film
WHERE (rating = 'G' or rating = 'PG-13') AND (length < 120) AND (rental_rate < 3.00)
ORDER BY title ASC;

-- Find a customer in the customer table, and change his/her details to your details, using SQL UPDATE
UPDATE customer
SET first_name ='Avvishek',
    last_name = 'Ramjeeawon',
    email = 'avithebest@hotmail.com'

WHERE first_name='Jared' AND last_name='Ely'
RETURNING 
    customer_id,
    first_name, 
    last_name,
    email;

-- Now find the customer’s address, 
-- and use UPDATE to change the address to your address (or make one up)
UPDATE address
set address = 'Roches Noires'
From customer
WHERE address.address_id = customer.address_id 
AND customer.first_name = 'Avvishek'
AND customer.last_name = 'Ramjeeawon';