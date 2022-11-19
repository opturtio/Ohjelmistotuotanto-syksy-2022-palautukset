*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  koira  koira123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123

Register With Too Short Username And Valid Password
    Input Credentials  k  kalle123

Register With Valid Username And Too Short Password
    Input Credentials  perro  a3

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  mummo  koirakoko


*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input Register Command