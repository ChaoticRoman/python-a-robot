*** Settings ***

Library  OperatingSystem


*** Keywords ***

vyprázdníme cech
    pycech  --clear

cech by měl být prázdný
    ${výstup} =  pycech  --status
    Should Be Equal  ${výstup}  ${EMPTY}


pycech
    [Arguments]  ${arg}
    ${výstup} =  Run  python3 ../scripts/cech.py ${arg}
    [Return]  ${výstup}
