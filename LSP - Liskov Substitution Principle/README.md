# [Liskov Substitution Principle (LSP)](https://en.wikipedia.org/wiki/Liskov_substitution_principle)

The Liskov Substitution Principle (LSP) is one of the principles from SOLID, which states that objects of a superclass should be able to be replaced with objects of a subclass without affecting the correctness of the program. In other words, a subclass should be able to override or extend the behavior of its superclass without violating the expected behavior of the superclass.

<br />

Here's an example in Python that illustrates the Liskov Substitution Principle:

In [bad.py](/LSP/bad.py) example, we have a Rectangle class with get_width, get_height, set_width, set_height, and area methods. We then create a Square class that inherits from the Rectangle class. However, the Square class overrides the set_width and set_height methods to enforce that both the width and height of a square should always be the same.

This violates the Liskov Substitution Principle, as the Square class changes the expected behavior of the Rectangle class. For example, if we have code that relies on the behavior of the Rectangle class, it may not work correctly with objects of the Square class, as the width and height of a Square object must always be the same.

> A better approach would be to properly adhere to the Liskov Substitution Principle.

In [good.py](/LSP/good.py) refactored version, the Square class does not violate the expected behavior of the Rectangle class. The set_width and set_height methods are kept, but additional methods specific to the Square class (set_side and get_side) are added, which do not override the behavior of the Rectangle class. This ensures that objects of the Square class can be safely used interchangeably with objects of the Rectangle class, adhering to the Liskov Substitution Principle.
