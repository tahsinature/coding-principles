# Good example following DRY

def calculate_tax(income):
  tax_rate = 0.3
  return income * tax_rate


def calculate_total_salary(income, bonus):
  tax = calculate_tax(income)
  return income + bonus - tax
