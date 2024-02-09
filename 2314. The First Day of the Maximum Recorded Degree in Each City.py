def find_the_first_day(weather: pd.DataFrame) -> pd.DataFrame:

    df = weather.sort_values(by=['city_id', 'degree', 'day'], ascending=[True, False, True])
    return df.groupby('city_id').head(1)