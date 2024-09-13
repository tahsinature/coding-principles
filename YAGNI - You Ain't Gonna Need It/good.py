# Good example following YAGNI

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

  # ... other necessary methods ...
