import pandas as pd


def create_bar_chart(sessions: pd.DataFrame) -> pd.DataFrame:
    bins = [0, 5 * 60, 10 * 60, 15 * 60, float('inf')]
    labels = ['[0-5>', '[5-10>', '[10-15>', '15 or more']

    # Use pd.cut to bin the durations
    sessions['bin'] = pd.cut(sessions['duration'], bins=bins, labels=labels, right=False)

    # Group by bin and count
    sessions = sessions.groupby('bin').size().reset_index(name='total')

    # Ensure all bins are present in the result
    df = pd.DataFrame({'bin': labels}).merge(sessions, on='bin', how='left').fillna(0)

    return df