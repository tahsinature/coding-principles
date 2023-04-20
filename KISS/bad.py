# Bad example violating KISS

def calculate_fibonacci(n):
  if n <= 0:
    return None
  elif n == 1:
    return 0
  elif n == 2:
    return 1
  else:
    return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)
