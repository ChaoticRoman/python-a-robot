*** Settings ***

Library  OperatingSystem


*** Keywords ***

vyprázdníme cech
    cech  --clear

cech by měl být prázdný
    ${výstup} =  cech  --status
    Should Be Equal  ${výstup}  ${EMPTY}


cech
    [Arguments]  ${arg}
    ${výstup} =  Run  python3 ../scripts/cech.py ${arg}
    [Return]  ${výstup}
