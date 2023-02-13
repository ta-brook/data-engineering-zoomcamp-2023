import pandas as pd
from sqlalchemy import create_engine
from time import time

def main():
    # improt data with pd
    df_iter = pd.read_csv('week_1_basics_n_setup/dataset/green_tripdata_2019-01.csv', iterator=True, chunksize=100000)
    # connect to db
    engine = create_engine('postgresql://postgres:postgres@localhost:5432/ny_taxi')
    # ingest taxi zones lookup
    df_zone = pd.read_csv('week_1_basics_n_setup/dataset/taxi+_zone_lookup.csv')
    df_zone.to_sql(name='zones', con=engine, if_exists='replace')

    while True:
        t_start = time()
        df = next(df_iter)
        df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
        df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)
        # commit to db
        df.to_sql(name='green_taxi_data', con=engine, if_exists='append')
        t_end = time()
        print(f"inserted another chunk..., took {t_end-t_start}.3f second")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: probably all data are inserted. but you can watch below about what is going on:\n {e}")