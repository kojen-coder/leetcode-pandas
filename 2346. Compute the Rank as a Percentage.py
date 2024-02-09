def compute_rating(students: pd.DataFrame) -> pd.DataFrame:
    df = students.copy()
    df["rank"] = df.groupby("department_id")['mark'].rank(method="min", ascending=False)
    df["stu_num"] = df.groupby("department_id")["department_id"].transform("count")
    df["percentage"] = np.where(
        df["stu_num"] > 1,
        round((df["rank"] - 1) * 100 / (df["stu_num"] - 1), 2), 0
    )

    return df.sort_values(["department_id", "percentage"], ascending = [True, True])[['student_id', 'department_id', 'percentage']]