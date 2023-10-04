import pandas as pd

def ads_performance(ads: pd.DataFrame) -> pd.DataFrame:
    ads.loc[ads['action'] == 'Clicked', 'clicked'] = 1
    ads.loc[ads['action'] == 'Viewed', 'viewed'] = 1
    df = ads.groupby('ad_id').agg(total_c=('clicked', 'sum'), total_v=('viewed', 'sum')).reset_index()
    df['ctr'] = (df['total_c'] / (df['total_c'] + df['total_v']) * 100).round(2).fillna(0)
    return df[['ad_id', 'ctr']].sort_values(['ctr', 'ad_id'], ascending=[False, True])
