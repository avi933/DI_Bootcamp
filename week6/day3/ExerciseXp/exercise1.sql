-- Get a list of all film languages
SELECT name 
FROM language;

-- Get a list of all films joined with their languages
-- select the following details : film title, description, and language name
SELECT film.title, film.description, language.name
FROM film
INNER JOIN language 
ON film.language_id = language.language_id;
-- 1.Get all films, even if they don’t have languages
SELECT film.title, film.description, language.name
FROM film
LEFT JOIN language 
ON film.language_id = language.language_id;
-- Get all languages, even if there are no films in those languages
SELECT film.title, film.description, language.name
FROM film
RIGHT JOIN language 
ON film.language_id = language.language_id;

-- Create a new table called new_film with the following columns 
-- id, name. Add some new films to the table.
CREATE TABLE new_film(
    new_film_id INTEGER primary key NOT NULL,
    name  VARCHAR NOT NULL);

INSERT INTO new_film (film_id,name)
 VALUES(1,'Ben Ten'),
       (4,'Martin Matin'),
       (9,'Teletubies');

CREATE TABLE customer_review(
    review_id serial NOT NULL,
    fk_film_id INTEGER,
    fk_language_id INTEGER,
    title VARCHAR(45),
    score SMALLINT,
    review_text VARCHAR,
    last_update date,
    PRIMARY KEY (review_id),
    FOREIGN KEY (fk_film_id) REFERENCES new_film(new_film_id) ON DELETE CASCADE,
    FOREIGN KEY (fk_language_id) REFERENCES language(language_id));

    -- Add 2 movie reviews. Make sure you link them to valid objects in the other tables.

    INSERT INTO customer_review(review_id,fk_film_id,fk_language_id,title,score,review_text,last_update)
     VALUES(1,1,1,'Ben Ten',7,'It is a nice movie','04/24/2020'),
           (2,4,1,'Martin Matin',9,'Awsome movie for kids','08/01/2020'),
           (3,9,1,'Teletubiess',1,'Boring movie','09/04/2021'),
           (4,1,1,'Ben Ten',9,'well loved by kids','10/01/2021');

-- Delete a film that has a review from the new_film table
-- what happens to the customer_review table?
DELETE FROM new_film where name = 'Teletubies';
-- ERROR: update or delete on table "new_film" violates foreign key constraint
-- "customer_review_fk_film_id_fkey" on table "customer_review"