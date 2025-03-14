# Write your MySQL query statement below
# first year of product then join, rank
with t as (
    select product_id, year as first_year,rank() over(partition by product_id order by year) as rn, quantity, price
    from Sales
)
select t.product_id, t.first_year, t.quantity, t.price
from t
where t.rn=1