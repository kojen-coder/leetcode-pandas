import pandas as pd

def team_size(employee: pd.DataFrame) -> pd.DataFrame:
    count = employee.groupby('team_id').size().reset_index(name='team_size')
    employee['team_size'] = employee['team_id'].map(count.set_index('team_id')['team_size'])
    return employee[['employee_id', 'team_size']]
