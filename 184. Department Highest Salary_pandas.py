import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    department.rename(columns={'id': 'departmentId', 'name': 'Department'}, inplace=True)
    employee.rename(columns={'name': 'Employee', 'salary': 'Salary'}, inplace=True)
    combine = pd.merge(employee, department, on='departmentId', how='left')
    result = combine.loc[combine.groupby('departmentId')['Salary'].transform('max') == combine['Salary']]
    return result[['Department', 'Employee', 'Salary']]
