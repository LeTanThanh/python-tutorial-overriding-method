from employee.base_employee import BaseEmployee
from employee.sales_employee import SalesEmployee

# Python Overriding Method

## Introduction to Python overridding method

john = SalesEmployee("John", 5_000, 15_000)
print(john.get_pay())

jane = BaseEmployee("Jane", 5_000)
print(jane.get_pay())
