import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    combined =  pd.merge(person, address, on='personId', how='left')
    return combined[['firstName', 'lastName', 'city', 'state']]
