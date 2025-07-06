import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    manager = employee[['id', 'salary']].rename(columns={'id': 'managerId', 'salary': 'manager_salary'})
    combined = pd.merge(employee, manager, on='managerId', how='left')
    ret = combined[combined['salary'] > combined['manager_salary']]
    return ret[['name']].rename(columns={'name': 'Employee'})
