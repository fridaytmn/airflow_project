import pandas as pd
from sqlalchemy import create_engine
import pyarrow.parquet as pq
from time import time
import os

def ingest_data(parquet_file, table_name):
    
    parquet_file = pq.ParquetFile(parquet_file)

    engine = create_engine(f"postgresql://root:root@de_postgres:5432/ny_taxi")

    for batch in parquet_file.iter_batches(batch_size=100000):
        t_start = time()
        batch_df = batch.to_pandas()
        batch_df.columns = [c.lower() for c in batch_df.columns]
        batch_df.to_sql(name=table_name, con=engine, if_exists="append", index=False)
        t_end = time()
        print("iserted next batch %.3f seconds" % (t_end - t_start))
