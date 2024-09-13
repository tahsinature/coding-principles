# [Single-Responsibility Principle (SRP)](https://en.wikipedia.org/wiki/Single-responsibility_principle)

The Single Responsibility Principle (SRP) is one of the principles from SOLID, a set of object-oriented design principles. SRP states that a class or module should have a single responsibility or reason to change. In other words, a class or module should have only one primary purpose or job, and it should not be responsible for multiple unrelated tasks. This promotes modularity, maintainability, and extensibility in software systems.

<br />

In [bad.py](/SRP/bad.py) example, the Employee class has multiple responsibilities. It has methods for calculating salary, generating payroll reports, and updating employee information. This violates the SRP, as the class is responsible for more than one task.

> A better approach would be to split the responsibilities into separate classes, each with its own single responsibility.

The [good.py](/SRP/good.py) is a refactored version, the Employee class only handles the attributes related to an employee, while the PayrollCalculator, PayrollReporter, and EmployeeInfoUpdater classes each handle a single responsibility related to payroll calculations, payroll reporting, and employee information updates, respectively. This adheres to the SRP, making the code more modular, maintainable, and extensible, as each class has a clear and single responsibility.
