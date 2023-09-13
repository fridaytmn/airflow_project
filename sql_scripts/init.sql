CREATE TABLE public.yellow_taxi_data (
	vendorid int4 NULL,
	tpep_pickup_datetime timestamp NULL,
	tpep_dropoff_datetime timestamp NULL,
	passenger_count float8 NULL,
	trip_distance float8 NULL,
	ratecodeid float8 NULL,
	store_and_fwd_flag text NULL,
	pulocationid int4 NULL,
	dolocationid int4 NULL,
	payment_type int8 NULL,
	fare_amount float8 NULL,
	extra float8 NULL,
	mta_tax float8 NULL,
	tip_amount float8 NULL,
	tolls_amount float8 NULL,
	improvement_surcharge float8 NULL,
	total_amount float8 NULL,
	congestion_surcharge float8 NULL,
	airport_fee float8 NULL
);