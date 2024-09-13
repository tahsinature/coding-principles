# Good example following KISS

def calculate_fibonacci(n):
  if n <= 0:
    return None
  a, b = 0, 1
  for _ in range(n-1):
    a, b = b, a + b
  return a
