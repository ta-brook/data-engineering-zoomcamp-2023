select * from green_taxi_data limit 5



select 
	count(1)
from 
	green_taxi_data 
where
	cast(lpep_pickup_datetime as date) = date '2019-01-15'
;



select 
	max(tip_amount) as tip,
	cast(lpep_pickup_datetime as date) as date
from 
	green_taxi_data 
group by
	date
order by
	tip desc
limit 1
;


select
	passenger_count, count(1)
from
	green_taxi_data gtd 
where
	cast(lpep_pickup_datetime as date) = date '2019-01-01'
group by
	passenger_count
;


select
	zndo."Zone",
	MAX(tip_amount) as tip
from
	green_taxi_data gtd 
inner join zones zndo
	on zndo."LocationID"  = gtd."DOLocationID" 
inner join zones znpu
	on znpu."LocationID" = gtd."PULocationID" 
where
	znpu."Zone" = 'Astoria'
group by
	1
order by
	tip DESC
;