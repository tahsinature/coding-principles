# Bad example violating DRY

def calculate_tax(income):
  tax_rate = 0.3
  return income * tax_rate


def calculate_total_salary(income, bonus):
  tax_rate = 0.3
  tax = income * tax_rate
  return income + bonus - tax
