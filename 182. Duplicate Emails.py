import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
   return person[person.duplicated(subset=['email'])][['email']].rename(columns={'email': 'Email'}).drop_duplicates()