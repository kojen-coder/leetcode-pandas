import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    df = project.merge(employee, on='employee_id', how='inner').reset_index()
    return df.groupby('project_id').agg(average_years=(
        'experience_years', lambda x: round(x.mean(), 2))).reset_index()
