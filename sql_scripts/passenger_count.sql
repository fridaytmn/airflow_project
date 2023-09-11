select COUNT(1) as freq, passenger_count
from yellow_taxi_data
group by passenger_count
order by freq desc