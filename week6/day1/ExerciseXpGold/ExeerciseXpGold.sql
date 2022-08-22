-- For the following questions, you have to fetch the first_names, last_names and birth_dates of the students.
-- Fetch the first four students. You have to order the four students alphabetically by last_name.

SELECT last_name, first_name , birth_date
FROM students
WHERE students_id = 1 OR students_id = 2 OR students_id = 3 OR students_id = 4
ORDER BY last_name ASC;

-- Fetch the details of the youngest student.
SELECT *
FROM students
ORDER BY birth_date DESC LIMIT 1;

--  Fetch three students skipping the first two students.
SELECT  first_name , last_name
FROM students  LIMIT 3 OFFSET 2;