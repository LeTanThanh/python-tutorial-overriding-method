import re

from .base_parser import BaseParser

class UkParser(BaseParser):
  phone_pattern = r"(\+\d{1}-\d{3}-\d{3}-\d{4})"
