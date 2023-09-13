from sqlalchemy import create_engine
import pyarrow.parquet as pq
from time import time
from os import environ
import dotenv

dotenv.load_dotenv(dotenv.load_dotenv())

def ingest_data(parquet_file, table_name):
    
    parquet_file = pq.ParquetFile(parquet_file)

    engine = create_engine(f"postgresql://{environ.get('PG_USER')}:{environ.get('PG_PASS')}@de_postgres:{int(environ.get('PG_PORT'))}/{environ.get('PG_DB')}")

    for batch in parquet_file.iter_batches(batch_size=100000):
        t_start = time()
        batch_df = batch.to_pandas()
        batch_df.columns = [c.lower() for c in batch_df.columns]
        batch_df.to_sql(name=table_name, con=engine, if_exists="append", index=False)
        t_end = time()
        print("iserted next batch %.3f seconds" % (t_end - t_start))
