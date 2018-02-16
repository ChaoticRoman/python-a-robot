*** Settings ***
Library    ./MyLibrary.py  32

*** Test Cases ***
Test of Python library
    ${out} =  get  10
    Log  ${out}
