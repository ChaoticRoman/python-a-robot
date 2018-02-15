*** Settings ***

Documentation     - kontrola vzniku uživateľa pri vzniku dlhu pokiaľ neexistuje
...               - kontrola pripisani dlhu pokiaľ uživatel niečo dlží

Resource   cech_resources.robot


*** Test Cases ***

Scénář prázdny cech
    vyprázdníme cech
    cech by měl být prázdný
