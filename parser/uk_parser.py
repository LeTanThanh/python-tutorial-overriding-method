import re

from .base_parser import BaseParser

class UkParser(BaseParser):
  def phone(self):
    match = re.search(r"(\+\d{1}-\d{3}-\d{3}-\d{4})", self.text)
    if match:
      return match.group(0)

    return None
