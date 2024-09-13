# Bad example violating YAGNI

class Employee:
  def __init__(self, name, age, salary):
    self.name = name
    self.age = age
    self.salary = salary

  def get_name(self):
    return self.name

  def get_age(self):
    return self.age

  def get_salary(self):
    return self.salary

  def get_tax(self):
    tax_rate = 0.3
    return self.salary * tax_rate

  def get_bonus(self):
    bonus = self.salary * 0.1
    return bonus

  # ... more methods ...
