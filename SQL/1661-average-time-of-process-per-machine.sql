# Write your MySQL query statement below
with end_temp as (
    select *
    from Activity
    where activity_type='end'
)
select s.machine_id,round(Avg(e.timestamp - s.timestamp),3) as processing_time
from Activity as s
left join end_temp as e
on s.machine_id = e.machine_id
and s.process_id = e.process_id
where s.activity_type='start'
group by s.machine_id