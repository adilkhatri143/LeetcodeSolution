-- Write your PostgreSQL query statement below
select p.project_id, round(avg(experience_years)::decimal, 2) as average_years
from Project as p, Employee as e
where p.employee_id = e.employee_id
group by p.project_id