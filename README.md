# Test project using pytest

This repository contain unit tests to "Employee" class, using the pytest library

Requirements

Python 3.x
Pytest 8.2.1

Installing the dependencies

pip install -r requirements.txt


# Tests
Tests are located in a "tests" folder in a class "tests_employee.py".
*fixture was not implemented yet.

## Test Cases

    Age Calculation:
        Case 1: When the idade method receives a date greater than the current year, it should return the message "Invalid date". This test checks if the date "01/01/2024" returns "Invalid date".
        Case 2: When the idade method receives a date in a different format than expected, it should fail. This test uses the xfail marker to indicate that the test is expected to fail when the date "01-01-2000" is provided, expecting the returned age to be 22.

    Last Name Return:
        Case 1: When the sobrenome method receives a full name with a last name, it should return the last name. This test checks if the name "Test Fulano Tests" returns "Tests".
        Case 2: When the sobrenome method receives only a single name without a last name, it should return the message "There isn't Last Name, please insert a Last Name!". This test checks if the name "Test" returns the expected message.

    Bonus Calculation:
        Case 1: When the calcular_bonus method receives a salary of 9999.90, it should return 999.99. This test verifies this specific calculation.
        Case 2: When the calcular_bonus method receives a salary of 10001, it should return 0. This test checks if the upper limit salary returns 0.
        Case 3: When the calcular_bonus method receives a salary of 10000.10, it should return 0. This test verifies if the salary slightly above the limit returns 0.
        Case 4: When the calcular_bonus method receives a negative salary, it should return the message "Invalid salary, please insert a valid salary". This test is marked with skip and checks if the negative salary returns the expected message.

## Test Execution
- To run all test write "-pytest" on the terminal.
- if you want to run tests related to a mark run this command "pytest -m mark_name".


This projects isn't finished yed. 



