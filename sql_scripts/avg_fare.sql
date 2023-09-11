SELECT
   passenger_count,
   avg(total_amount)
FROM yellow_taxi_data
GROUP BY passenger_count;