-- Use UPDATE to change the language of some films. 
-- Make sure that you use valid languages.
-- 1-English,2-Italian,3-Japanese,4-Mandarin,5-French,6-German  
UPDATE film
SET language_id = '2' 
WHERE film_id = 98;

UPDATE film
SET language_id = '4' 
WHERE film_id = 8;

UPDATE film
SET language_id = '6' 
WHERE film_id = 11;

-- Which foreign keys (references) are defined for the customer table? 
-- How does this affect the way in which we INSERT into the customer table?
-- store_id / address_id

-- We created a new table called customer_review. 
-- Drop this table. Is this an easy step, or does it need extra checking?
DROP TABLE IF EXISTS customer_review;

-- Find out how many rentals are still outstanding 
-- (ie. have not been returned to the store yet).
SELECT count(*)
From rental
where return_date ISNULL;

-- Find the 30 most expensive movies which are outstanding
-- (ie. have not been returned to the store yet)
SELECT film.title, film.replacement_cost
FROM film
INNER JOIN inventory
ON film.film_id = inventory.film_id
INNER JOIN rental 
ON inventory.inventory_id = rental.inventory_id
WHERE rental.rental_date ISNULL
ORDER BY film.replacement_cost DESC LIMIT 30;

-- Can you help him find which movies he wants to rent?
-- The 1st film : The film is about a sumo wrestler
-- and one of the actors is Penelope Monroe.
SELECT title
FROM film_list
WHERE actors like '%Penelope Monroe%'
AND lower(description) like '%sumo wrestler%';

-- The 2nd film : A short documentary (less than 1 hour long), rated “R”.
SELECT title 
FROM film
WHERE length < 60 and rating = 'R';

-- The 3rd film : A film that his friend Matthew Mahan rented. 
-- He paid over $4.00 for the rental, 
-- and he returned it between the 28th of July and the 1st of August, 2005.
SELECT film.title
From rental
INNER JOIN customer
ON rental.customer_id = customer.customer_id
INNER JOIN inventory
ON rental.inventory_id = inventory.inventory_id
INNER JOIN film
ON inventory.film_id = film.film_id
WHERE film.rental_rate > 4.00 
AND (rental.return_date BETWEEN '07/28/2005' AND '08/01/2005' )
AND customer.first_name = 'Matthew' 
ANd customer.last_name = 'Mahan';

-- The 4th film : His friend Matthew Mahan watched this film, as well. 
-- It had the word “boat” in the title or description
-- and it looked like it was a very expensive DVD to replace.
SELECT customer.first_name, film.title,film.replacement_cost
From customer
Inner JOIN rental
ON customer.customer_id = rental.customer_id
Inner JOIN inventory
ON rental.inventory_id = inventory.inventory_id
INNER JOIN film
ON inventory.film_id = film.film_id
WHERE customer.first_name = 'Matthew' AND customer.last_name = 'Mahan' 
AND (lower(film.description) like '%boat%'
OR lower(film.title) like '%boat%') 
ORDER by film.replacement_cost DESC;

