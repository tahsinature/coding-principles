# [Interface Segregation Principle (ISP)](https://en.wikipedia.org/wiki/Interface_segregation_principle)

The Interface Segregation Principle (ISP) is another principle from SOLID, which states that clients should not be forced to depend on interfaces they don't use. In other words, interfaces should be specific to the needs of the clients that use them, rather than being overly general.

<br />

Here's an example in Python that illustrates the ISP principle:

In [bad.py](/ISP/bad.py) example, we have a Printer interface with print, fax, and scan methods. We then create a MultifunctionalPrinter class that implements the Printer interface. However, this violates the Interface Segregation Principle, as the MultifunctionalPrinter class is forced to implement all the methods of the Printer interface, even though it may not use all of them. This can result in bloated classes with unnecessary methods, and clients may be forced to depend on methods they don't need or use.

> A better approach would be to adhere to the Interface Segregation Principle by creating more specific interfaces.

The [good.py](/ISP/good.py) is a refactored version, we have created separate interfaces for Printer, Fax, and Scanner, each with their own specific methods. The MultifunctionalPrinter class then implements only the interfaces it needs (Printer, Fax, and Scanner), and it is not forced to implement unnecessary methods. This ensures that clients can depend only on the specific interfaces they need, adhering to the Interface Segregation Principle.
