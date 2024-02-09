def arrange_table(genders: pd.DataFrame) -> pd.DataFrame:
    genders['rank'] = genders.groupby ( 'gender' )['user_id'].rank ( method='first', ascending=True )
    genders.loc[genders['gender'] == 'female', 'flag'] = 1
    genders.loc[genders['gender'] == 'other', 'flag'] = 2
    genders.loc[genders['gender'] == 'male', 'flag'] = 3

    return genders.sort_values ( ['rank', 'flag'], ascending=[True, True] )[['user_id', 'gender']]
