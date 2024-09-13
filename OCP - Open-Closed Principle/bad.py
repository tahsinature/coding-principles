# Bad example violating OCP

class PaymentProcessor:
  def process_payment(self, payment):
    if payment.method == 'credit_card':
      # Code to process credit card payment
      pass
    elif payment.method == 'paypal':
      # Code to process PayPal payment
      pass
    elif payment.method == 'bank_transfer':
      # Code to process bank transfer payment
      pass
    else:
      # Code for other payment methods
      pass
