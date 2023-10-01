import pandas as pd


def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame,
                              examinations: pd.DataFrame) -> pd.DataFrame:
    df = students.merge(subjects, how='cross').sort_values(['student_id', 'subject_name'])
    df1 = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')
    return df.merge(df1, on=['student_id', 'subject_name'], how='left').rename(
        columns={'subject_name_x': 'subject_name'}).fillna(0)[
        ["student_id", 'student_name', 'subject_name', 'attended_exams']]

