*** Settings ***
Suite Setup       Setup Actions
Suite Teardown    Teardown Actions
Test Setup        Log  test setup
Test Teardown     Log  test teardown

*** Test Cases ***
Some test case 1
    Sleep    0.1
    Log    Test 1

Some test case 2
    [Setup]     Log  Custom setup
    Sleep       0.1
    Log         Test 2
    [Teardown]  Log  Custom teardown

*** Keywords ***
Setup Actions
    Log    Setup Actions done here

Teardown Actions
    Log    Teardown Actions done here
