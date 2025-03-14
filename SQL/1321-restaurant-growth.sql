# Write your MySQL query statement below
select visited_on,amount,average_amount from 
(with t as (
    select visited_on,sum(amount) as amount,1 as cnt
    from Customer
    group by visited_on
)
select visited_on, sum(amount) over(order by visited_on rows between 6 PRECEDING and current row) as amount, round(avg(amount) over (order by visited_on rows between 6 PRECEDING and current row),2) as average_amount, sum(cnt) over(order by visited_on) as fil
from t) tt
where fil>6