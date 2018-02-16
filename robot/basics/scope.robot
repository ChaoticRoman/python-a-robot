*** Test cases ***
test 1
    set      SUCCESS
    check

*** Keywords ***
set
    [Arguments]        ${arg}
    ${STATUS} =        Set variable  ${arg}
    Set Test Variable  ${STATUS}

check
    Should Be Equal    ${STATUS}   SUCCESS
