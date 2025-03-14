# Write your MySQL query statement below
# group by student_id, subject_name, count(subject_name) as attended_exams
with res as (
    select student_id, subject_name, count(subject_name) as cnt
    from Examinations
    group by student_id, subject_name
)
-- select r.student_id,s.student_name, r.subject_name, r.cnt as attended_exams
-- from res as r
-- outer join Students as s
-- on r.student_id = s.student_id
-- select e.*
-- from Examinations as e
-- right join Subjects as sub
-- on e.subject_name = sub.subject_name
select s.student_id,s.student_name, sub.subject_name,  case when r.cnt is null then 0 else r.cnt
end as attended_exams
from Students as s
join Subjects as sub
left join res as r
on r.student_id = s.student_id
and r.subject_name = sub.subject_name
order by s.student_id, sub.subject_name