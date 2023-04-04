0x07. Python - Test-driven development



Testing is crucial in the software development phase. It helps ensure easy debugging, agile code, and enhanced reusability. Performing tests that cover all use cases helps prevent a codebase from breaking — minimizing exposure to vulnerabilities. Python has two main testing frameworks that developers can use, doctest and unittest.


What is Doctest?
Doctest is an inbuilt test framework that comes bundled with Python by default. The doctest module searches for code fragments that resemble interactive Python sessions and runs those sessions to confirm they operate as shown.

Developers commonly use doctest to test documentation. The doctest module looks for sequences of prompts in a docstring, re-executes the extracted command, and compares the output with the command’s input given in the docstrings test example.

The default action when running doctests is not to show the output when a test passes. However, we can change this in the doctest runner options. In addition, doctest’s integration with the Python unittest module enables us to run doctests as standard unittest test cases.




What is Unittest?
Unittest test case runners allow more options when running tests, like reporting test statistics such as tests that passed and failed.

Unittest uses methods created in classes to manage tests. It has support for automation, setup, and shutdown code when testing. Unittest has several rich, in-built features that are unavailable in doctest, including generators and group fixture managers like setUp and tearDown. 

Since unittest follows the object-oriented method, it’s more suitable for testing class-based methods in a non-production environment. Continuous delivery tools such as Jenkins or Travis CI work better for production environments.
We’ll create a real-world example in the following sections, some code with customer information and discounts, and test it using doctest and unittest. Then we’ll analyze the tests and recommend the best ways to make further improvements.  
