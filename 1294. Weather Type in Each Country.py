import pandas as pd

def weather_type(countries: pd.DataFrame, weather: pd.DataFrame) -> pd.DataFrame:
    df = weather[(weather['day'] >= '2019-11-01') & (weather['day'] <= '2019-11-30')]
    if df.shape[0] == 0:
        df[["country_name", "weather_type"]] = None
        return df[["country_name", "weather_type"]]
    df = df \
        .merge(countries, on='country_id', how='inner') \
        .groupby('country_name').agg(weather_type=('weather_state', 'mean')).reset_index()
    if df.shape[0] == 0:
        return pd.DataFrame({"country_name": [None], "weather_type": [None]})
    df.loc[df['weather_type'] <= 15, 'weather_type2'] = 'Cold'
    df.loc[df['weather_type'] >= 25, 'weather_type2'] = 'Hot'
    df['weather_type2'] = df['weather_type2'].fillna('Warm')
    return df[['country_name', 'weather_type2']].rename(columns={"weather_type2": "weather_type"})

