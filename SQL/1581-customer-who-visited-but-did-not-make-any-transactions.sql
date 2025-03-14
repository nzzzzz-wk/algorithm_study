# Write your MySQL query statement below
with temp_table as (
    select a.visit_id,a.customer_id,b.transaction_id
    from Visits as a
    left join Transactions as b
    on a.visit_id = b.visit_id
    where b.transaction_id is null
)
select customer_id,count(visit_id) as count_no_trans
from temp_table
group by customer_id