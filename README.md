## Overview
This program is a command-line tuition calculation system developed in Python.  It demonstrates foundational Object-Oriented Design (OOD) principles, specifically the Strategy Design Pattern.
By dynamically applying different discount behaviors to student tuition without altering the core checkout logic.
## Architecture
The system is built using interrelated classes that separate the main checkout context from the specific discount calculation algorithms:
1. StudentDiscount Class: Serves as the abstract base strategy (or interface) for individual discount tiers. It defines the required apply_discount() method that all concrete discount implementations must follow.
2. Concrete Strategy Classes (PL, DL, NoDiscount): Act as the specific implementations of the discount behavior. They encapsulate the exact logic for applying 100%, 50%, and 0% tuition reductions, respectively, keeping the calculation logic safely isolated.
3. Checkout Class: Acts as the context manager. It stores a reference to a StudentDiscount strategy object and handles overarching system operations. This includes dynamically calculating the final total by delegating the math to the injected strategy's apply_discount() method.

```
+-------------------------+          +-------------------------+
|        Checkout         |          |     StudentDiscount     |
+-------------------------+          +-------------------------+
| - strategy:             | <>------ |                         |
|     StudentDiscount     |  (uses)  |                         |
+-------------------------+          +-------------------------+
| + calculate_total()     |          | + apply_discount()      |
+-------------------------+          +-------------------------+
                                                  ^
                                                  |
              +-----------------------------------+-----------------------------------+
              |                                   |                                   |
+-------------------------+          +-------------------------+          +-------------------------+
|           PL            |          |           DL            |          |       NoDiscount        |
+-------------------------+          +-------------------------+          +-------------------------+
| + apply_discount()      |          | + apply_discount()      |          | + apply_discount()      |
+-------------------------+          +-------------------------+          +-------------------------+
```
## How to Run
1. Ensure Python3 is installed.
2. Run the unit tests: python3 -m unittest test_main.py -v
3. The results show 3 passing tests (test_pl_discount, test_dl_discount, test_no_discount), each confirming that the correct discount strategy produces the expected tuition total. A final "OK" confirms all tests passed.
