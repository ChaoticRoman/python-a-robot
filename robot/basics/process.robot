*** Settings ***
Library  Process

*** Test Cases ***
Using Kwargs
    Run Program    .     -iname\=*.robot  shell=True
    Run Program    ..    -name\=hello.*

** Keywords ***
Run Program
    [Arguments]          @{arguments}  &{configuration}
    Run Process    find  @{arguments}  &{configuration}
