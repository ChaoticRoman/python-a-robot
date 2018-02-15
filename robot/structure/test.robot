*** Settings ***
Resource   my_resources.robot
Variables  vars.py

*** Test Cases ***
Test Robot Framework Logging
    [Tags]  some tag  tag2
    Log    "Test Logging"

Test My Logging
    [Tags]  some tag  tag3
    My Logging   "Test My Logging 1"   "Test My Logging 2"
    My Logging   ${a}  ${b}  ${c}

