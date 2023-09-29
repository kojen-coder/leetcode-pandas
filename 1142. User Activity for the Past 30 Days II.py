import pandas as pd


def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity[(activity['activity_date'] > '2019-06-27') & (activity['activity_date'] <= '2019-07-27')]
    if df.shape[0] == 0:
        return pd.DataFrame({'average_sessions_per_user': [0]})
    user_session = df.groupby('user_id')['session_id'].nunique().reset_index(name='total')
    result = round(user_session['total'].mean(), 2)

    return pd.DataFrame({'average_sessions_per_user': [result]})