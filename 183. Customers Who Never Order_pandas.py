import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    customers.rename(columns={'id': 'customerId'}, inplace=True)
    combined = pd.merge(customers, orders, on='customerId', how='left')
    combined.fillna({'id': -1}, inplace=True)
    combined.rename(columns={'name': 'Customers'}, inplace=True)
    return combined.loc[combined['id'] == -1, ['Customers']]
