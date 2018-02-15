*** Settings ***
Library  OperatingSystem


*** Test cases ***
Test 1
    Ulož globální hodnotu "ABC"
    Testuj, zda je globální hodnota "ABC"


*** Keywords ***
Ulož globální hodnotu "ABC"
    ${output} =  Run  echo ABC
    set suite variable  ${globalizácia}  ${output}

Testuj, zda je globální hodnota "ABC"
    Log  ${globalizácia}
    Should Be Equal  ${globalizácia}  ABC
