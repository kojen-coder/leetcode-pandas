def driver_passenger(rides: pd.DataFrame) -> pd.DataFrame:
    df = rides.groupby('passenger_id').agg(cnt=('passenger_id', 'size')).reset_index()
    return df.merge(rides, left_on='passenger_id', right_on='driver_id', how='right')\
                    .fillna(0)[['driver_id', 'cnt']].drop_duplicates()