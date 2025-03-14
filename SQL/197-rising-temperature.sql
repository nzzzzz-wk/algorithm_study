# Write your MySQL query statement below
with y_temp as (
    select *,recordDate + INTERVAL 1 DAY AS y_date
    from Weather
)

select t.id
from Weather as t
left join y_temp as y
on t.recordDate = y.y_date
where t.Temperature>y.Temperature
