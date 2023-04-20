# [Open-Closed Principle (OCP)](https://en.wikipedia.org/wiki/Open–closed_principle)

The Open/Closed Principle (OCP) is another principle from SOLID, which states that code should be open for extension but closed for modification. In other words, once a class or module is implemented and tested, it should be closed for modification, but it should be open for extension by adding new functionality without modifying its existing code. This promotes code stability, reusability, and maintainability.

<br />

Here's an example in Python that illustrates the OCP principle:

In [bad.py](/OCP/bad.py) example, the PaymentProcessor class has a single method process_payment that handles different payment methods (credit card, PayPal, bank transfer, etc.) using conditional statements. This violates the OCP, as adding a new payment method would require modifying the existing code of the PaymentProcessor class.

A better approach would be to use abstraction and interfaces to allow for extension without modifying the existing code.

The [good.py](/OCP/good.py) is a refactored version, the PaymentProcessor class is open for extension as new payment processors can be added without modifying its code. Each payment processor is implemented as a separate class that conforms to the PaymentProcessorInterface interface, which defines the process method. This allows for easy extension and customization of the payment processing behavior without modifying the existing code of the PaymentProcessor class, thus adhering to the OCP principle.
