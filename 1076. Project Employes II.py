import pandas as pd

def project_employees_ii(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    df = project.groupby('project_id')['employee_id'].size().reset_index(name='count').sort_values('count', ascending=False)
    return df[df['count'] == df['count'].max()][['project_id']]