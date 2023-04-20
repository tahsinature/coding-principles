# Good example following OCP

class PaymentProcessor:
  def process_payment(self, payment):
    payment_processor = self.get_payment_processor(payment.method)
    payment_processor.process(payment)

  def get_payment_processor(self, method):
    # Factory method to get the appropriate payment processor
    if method == 'credit_card':
      return CreditCardProcessor()
    elif method == 'paypal':
      return PayPalProcessor()
    elif method == 'bank_transfer':
      return BankTransferProcessor()
    else:
      return DefaultPaymentProcessor()


class PaymentProcessorInterface:
  def process(self, payment):
    pass


class CreditCardProcessor(PaymentProcessorInterface):
  def process(self, payment):
    # Code to process credit card payment
    pass


class PayPalProcessor(PaymentProcessorInterface):
  def process(self, payment):
    # Code to process PayPal payment
    pass


class BankTransferProcessor(PaymentProcessorInterface):
  def process(self, payment):
    # Code to process bank transfer payment
    pass


class DefaultPaymentProcessor(PaymentProcessorInterface):
  def process(self, payment):
    # Code for other payment methods
    pass
