SELECT * FROM classes;

SELECT "name", credits FROM classes WHERE credits > 3;

SELECT * FROM classes WHERE mod(credits, 2) = 0;

SELECT * FROM enrollments WHERE student_id = 1 AND grade IS NULL; 

SELECT enrollments.id, student_id, class_id, grade 
    FROM enrollments 
    INNER JOIN students ON student_id = students.id 
    WHERE first_name = 'Tianna' AND grade IS NULL;

SELECT enrollments.id, student_id, class_id, "name", grade 
    FROM enrollments 
    INNER JOIN students ON student_id = students.id
    INNER JOIN classes ON class_id = classes.id
    WHERE first_name = 'Tianna' AND grade IS NULL;  

SELECT EXTRACT(YEAR FROM AVG(AGE(current_date, birthdate))) FROM students;

SELECT * FROM addresses WHERE city LIKE '% %';

SELECT * FROM students 
    INNER JOIN ADDRESSES ON address_id = addresses.id 
    WHERE city LIKE '% %';

SELECT AVG(credits) FROM classes;  

SELECT first_name, last_name FROM students 
    INNER JOIN enrollments ON student_id = students.id 
    WHERE grade = 'A'; 

SELECT students.first_name, SUM(credits) FROM enrollments 
    INNER JOIN students ON students.id = student_id 
    INNER JOIN classes ON classes.id = class_id 
    GROUP BY students.first_name;