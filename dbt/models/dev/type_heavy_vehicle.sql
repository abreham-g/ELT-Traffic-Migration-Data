{{ config(materialized='table') }}

select * from {{ ref('open_traffic_all') }} where type = 'Heavy Vehicle'
