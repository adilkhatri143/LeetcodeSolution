-- Write your PostgreSQL query statement below
select p.project_id, round(sum(experience_years) / count(p.project_id)::decimal, 2) as average_years
from Project as p, Employee as e
where p.employee_id = e.employee_id
group by p.project_id