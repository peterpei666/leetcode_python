import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
   email = person.groupby('email').size().reset_index(name='count')
   email = email[email['count'] > 1]
   return email[['email']].rename(columns={'email': 'Email'})
