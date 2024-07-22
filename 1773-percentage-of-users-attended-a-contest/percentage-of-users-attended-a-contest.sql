-- Write your PostgreSQL query statement below
SELECT R.contest_id, ROUND(COUNT(U.user_id) * 100 / (SELECT COUNT(user_id) from Users)::decimal, 2) as percentage
FROM Register as R INNER JOIN Users as U
ON R.user_id = U.user_id
group by R.contest_id
order by percentage DESC, R.contest_id