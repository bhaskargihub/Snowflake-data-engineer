-- dbt model: transforms raw sales into analytics-ready table
with base as (
    select
        id,
        to_date(date) as date,
        amount
    from {{ source('public', 'sales_data_raw') }}
)

select
    id,
    date,
    amount,
    amount * 1.18 as amount_with_tax
from base
