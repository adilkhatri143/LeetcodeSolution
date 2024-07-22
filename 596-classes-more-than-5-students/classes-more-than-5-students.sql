-- Write your PostgreSQL query statement below
SELECt class
FROM Courses
Group by class
HAVING COUNT(class) >= 5;