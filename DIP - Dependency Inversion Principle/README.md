# [Dependency Inversion Principle (DIP)](https://en.wikipedia.org/wiki/Dependency_inversion_principle)

The Dependency Inversion Principle (DIP) is the last principle in SOLID, which states that high-level modules should not depend on low-level modules, but both should depend on abstractions. It also emphasizes that abstractions should not depend on details, but details should depend on abstractions.

<br />

Here's an example in Python that illustrates the DIP principle:

In [bad.py](/DIP/bad.py) example, we have a NotificationService class that depends directly on a EmailSender class, which is a low-level module. This violates the Dependency Inversion Principle, as the high-level NotificationService class is tightly coupled to the low-level EmailSender class, making it difficult to change or extend the system without impacting the NotificationService class.

> A better approach would be to adhere to the Dependency Inversion Principle by introducing abstractions and using dependency injection.

The [good.py](/DIP/good.py) is a refactored version, we have introduced an abstraction NotificationSender and created a concrete implementation EmailNotificationSender that depends on EmailSender, a low-level module. The NotificationService class now depends on the abstraction NotificationSender instead of the concrete EmailSender, which allows for flexibility and extensibility. The concrete implementation can be easily changed or extended without impacting the NotificationService class, adhering to the Dependency Inversion Principle.
