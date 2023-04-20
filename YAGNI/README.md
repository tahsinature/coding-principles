# [You Ain't Gonna Need It (YAGNI)](https://en.wikipedia.org/wiki/You_aren't_gonna_need_it)

The You Ain't Gonna Need It (YAGNI) principle is a software development principle that advises against adding unnecessary features or functionality to a system.

<br />

Here's an example in Python that illustrates the YAGNI principle:

In [bad.py](/YAGNI/bad.py) example, we have an Employee class with several methods such as get_name(), get_age(), get_salary(), get_tax(), and get_bonus(). However, some of these methods such as get_tax() and get_bonus() are not currently used in the system and add unnecessary complexity to the codebase, violating the YAGNI principle.

> A better approach would be to adhere to the YAGNI principle by only including the necessary features.

In [bad.py](/YAGNI/good.py) example, we have removed the unnecessary methods get_tax() and get_bonus() as they are not currently used in the system, adhering to the YAGNI principle and keeping the codebase simple and focused on the necessary functionality.
