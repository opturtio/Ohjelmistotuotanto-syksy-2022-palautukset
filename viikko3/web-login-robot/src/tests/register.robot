*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Register Page Should Be Open
    Set Username  koira
    Set Password  koira123
    Set Password Confirmation  koira123

Register With Too Short Username And Valid Password
    Register Page Should Be Open
    Set Username  k
    Set Password  koira123
    Set Password Confirmation  koira123
    Submit Credentials Register
    Register Should Fail With Message  Too short username

Register With Valid Username And Too Short Password
    Register Page Should Be Open
    Set Username  kissa
    Set Password  k
    Set Password Confirmation  k
    Submit Credentials Register
    Register Should Fail With Message  Too short password

Register With Nonmatching Password And Password Confirmation
    Register Page Should Be Open
    Set Username  kissa
    Set Password  koira123
    Set Password Confirmation  koira321
    Submit Credentials Register
    Register Should Fail With Message  Check you password

Login After Successful Registration
    Create User And Go To Login Page
    Set Username  kalle
    Set Password  kalle123
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  pena
    Set Password  pelle
    Set Password Confirmation  pelle
    Go To Login Page
    Login Page Should Be Open
    Set Username  pena
    Set Password  pelle
    Submit Credentials
    Login Should Fail With Message  Invalid username or password