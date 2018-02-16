*** Settings ***
Library  OperatingSystem

*** Test Cases ***
Testing bash commands
    Log  Hello World!

    ${status} =  Run And Return Rc  true
    ${status} =  Convert To String  ${status}
    Should be Equal  ${status}  0

    ${status} =  Run And Return Rc  false
    # ${status} =  Convert To String  ${status}
    Should be Equal  ${status}  ${1}
