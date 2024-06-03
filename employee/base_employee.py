class BaseEmployee:
  def __init__(self, name, base_pay) -> None:
    self.name = name
    self.base_pay = base_pay

  def get_pay(self):
    return self.base_pay
