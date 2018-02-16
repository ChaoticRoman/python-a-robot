*** Settings ***
Library    MyLibrary       32
Library    AnotherLibrary

*** Test Cases ***
Test of Python library
    ${out} =  get  10
    Log  ${out}

Test 1
    Call some function

Test 2
    ${out} =  Call some function
    Log  ${out}
