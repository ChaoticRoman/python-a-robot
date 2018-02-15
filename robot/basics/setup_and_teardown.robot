*** Settings ***
Suite Setup       Setup Actions
Suite Teardown    Teardown Actions

*** Test Cases ***
Some test case 1
    Log    Test 1

Some test case 2
    Log    Test 2

*** Keywords ***
Setup Actions
    Log    Setup Actions done here

Teardown Actions
    Log    Teardown Actions done here
