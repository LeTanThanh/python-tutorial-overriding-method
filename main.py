from employee.base_employee import BaseEmployee
from employee.sales_employee import SalesEmployee

from parser.base_parser import BaseParser
from parser.uk_parser import UkParser

# Python Overriding Method

## Introduction to Python overridding method

john = SalesEmployee("John", 5_000, 15_000)
print(john.get_pay())

jane = BaseEmployee("Jane", 5_000)
print(jane.get_pay())

## Advanced method overriding example

s1 = "Contact us via 408-205-5663 or email@test.com"
base_parser = BaseParser(s1)
print(base_parser.parse())

s2 = "Contact me via +1-650-453-3456 or email@test.co.uk"
uk_parser = UkParser(s2)
print(uk_parser.parse())
