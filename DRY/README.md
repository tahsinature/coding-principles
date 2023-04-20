# [Don't Repeat Yourself (DRY)](https://en.wikipedia.org/wiki/Don't_repeat_yourself)

The Don't Repeat Yourself (DRY) principle is a software development principle that promotes code reusability and maintainability by avoiding duplication of code.

<br />

Here's an example in Python that illustrates the DRY principle:

In [bad.py](/DRY/bad.py) example, we have duplicated the tax rate calculation logic in two different functions calculate_tax() and calculate_total_salary(). This violates the DRY principle, as the same tax rate calculation is repeated, leading to potential maintenance issues if the tax rate changes in the future.

> A better approach would be to adhere to the DRY principle by removing the code duplication and promoting code reusability.

The [good.py](/DRY/good.py) is a refactored version, we have extracted the tax rate calculation logic into a separate function calculate_tax() and called it from the calculate_total_salary() function. This promotes code reusability and maintainability, as changes to the tax rate calculation can be made in one place without duplicating code, adhering to the DRY principle.
