*** Settings ***
Documentation    Suite-level documentation
Resource         my_resources.robot
Variables        vars.py

*** Test Cases ***
Test Robot Framework Logging
    [Documentation]    We are testing
    [Tags]  some tag  tag2
    Log    "Test Logging"

Test My Logging
    [Documentation]   Test the world out!
    [Tags]  some tag  tag3
    My Logging   "Test My Logging 1"   "Test My Logging 2"
    My Logging   ${a}  ${b}  ${c}
    MY Logging   @{list}
    Log          &{dictionary}[0.3]
