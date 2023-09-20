import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    repeat = my_numbers['num'].duplicated(keep=False)
    clean = my_numbers[~repeat]
    num = None if clean.shape[0] == 0 else clean['num'].max()
    return pd.DataFrame({'num': [clean['num'].max()]})